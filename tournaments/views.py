from django.shortcuts import render, redirect
from .models import Joueur, Tournoi, Match

def inscrire_joueur(request, tournoi_id):
    tournoi = Tournoi.objects.get(id=tournoi_id)
    
    if request.method == 'POST':
        nom_joueur = request.POST['nom']
        joueur = Joueur.objects.create(nom=nom_joueur, tournoi=tournoi)
        joueur.save()
        return redirect('tournoi_bracket', tournoi_id=tournoi.id)  # Rediriger vers la page du bracket après inscription
    
    return render(request, 'inscrire_joueur.html', {'tournoi': tournoi})

def tournoi_bracket(request, tournoi_id):
    tournoi = Tournoi.objects.get(id=tournoi_id)
    joueurs = Joueur.objects.filter(tournoi=tournoi)
    
    return render(request, 'tournoi_bracket.html', {'joueurs': joueurs})

from django.shortcuts import render
from .models import Tournoi, Match  # Assurez-vous d'importer Tournoi et Match

def accueil(request):
    tournoi = Tournoi.objects.get(id=1)  # Récupère le premier tournoi ou un tournoi spécifique
    quart_de_finale = Match.objects.filter(tournoi=tournoi, round='Quart de finale')
    demi_finale = Match.objects.filter(tournoi=tournoi, round='Demi-finale')
    finale = Match.objects.filter(tournoi=tournoi, round='Finale')

    return render(request, 'tournaments/accueil.html', {
        'tournoi': tournoi,
        'quart_de_finale': quart_de_finale,
        'demi_finale': demi_finale,
        'finale': finale
    })

def mettre_a_jour_gagnant(match):
    if match.score_participant1 > match.score_participant2:
        match.gagnant = match.participant1
    elif match.score_participant2 > match.score_participant1:
        match.gagnant = match.participant2
    match.save()

def afficher_tournoi(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi, id=tournoi_id)

    # Récupérer les matchs en fonction du tour
    quart_de_finale = Match.objects.filter(tour='quart', participant1__tournoi=tournoi)
    demi_finale = Match.objects.filter(tour='demi', participant1__tournoi=tournoi)
    finale = Match.objects.filter(tour='finale', participant1__tournoi=tournoi)
    champion = Match.objects.filter(tour='champion', participant1__tournoi=tournoi).first()

    return render(request, 'tournaments/accueil.html', {
        'tournoi': tournoi,
        'quart_de_finale': quart_de_finale,
        'demi_finale': demi_finale,
        'finale': finale,
        'champion': champion
    })