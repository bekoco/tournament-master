from django.shortcuts import get_object_or_404, render, redirect
from .models import Joueur, Tournoi, Match

# Inscription d'un joueur
def inscrire_joueur(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi, id=tournoi_id)
    
    if request.method == 'POST':
        nom_joueur = request.POST['nom']
        joueur = Joueur.objects.create(nom=nom_joueur, tournoi=tournoi)
        return redirect('afficher_tournoi', tournoi_id=tournoi.id)
    
    return render(request, 'tournaments/inscrire_joueur.html', {'tournoi': tournoi})

# Affichage du bracket et des matchs par tour
def afficher_tournoi(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi, id=tournoi_id)

    # Récupérer les matchs et les classer par round (tour)
    quart_de_finale = Match.objects.filter(round='Quart de finale', tournoi=tournoi)
    demi_finale = Match.objects.filter(round='Demi-finale', tournoi=tournoi)
    finale = Match.objects.filter(round='Finale', tournoi=tournoi)
    champion = Match.objects.filter(round='Champion', tournoi=tournoi).first()

    return render(request, 'tournaments/accueil.html', {
        'tournoi': tournoi,
        'quart_de_finale': quart_de_finale,
        'demi_finale': demi_finale,
        'finale': finale,
        'champion': champion
    })

# Liste des tournois
def liste_tournois(request):
    tournois = Tournoi.objects.all()  # Récupère tous les tournois
    return render(request, 'tournaments/liste_tournois.html', {'tournois': tournois})


# Accueil
def accueil(request):
    return render(request, 'tournaments/accueil.html')
