from django.shortcuts import render, redirect
from .models import Joueur, Tournoi

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

def accueil(request):
    return render(request, 'tournaments/accueil.html')

from django.shortcuts import render, get_object_or_404
from .models import Tournoi, Match

def afficher_tournoi(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi, id=tournoi_id)
    matchs = Match.objects.filter(participant1__tournoi=tournoi)
    
    return render(request, 'tournaments/tournoi_bracket.html', {
        'tournoi': tournoi,
        'matchs': matchs
    })

def mettre_a_jour_gagnant(match):
    if match.score_participant1 > match.score_participant2:
        match.gagnant = match.participant1
    elif match.score_participant2 > match.score_participant1:
        match.gagnant = match.participant2
    match.save()

def afficher_tournoi(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi, id=tournoi_id)
    matchs = Match.objects.filter(participant1__tournoi=tournoi)

    # Mettre à jour les gagnants
    for match in matchs:
        mettre_a_jour_gagnant(match)

    return render(request, 'tournaments/tournoi_bracket.html', {
        'tournoi': tournoi,
        'matchs': matchs
    })