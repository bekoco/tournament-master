# tournaments/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Tournoi, Participant, Match
from django.http import HttpResponse
import os


def accueil(request):
    return render(request, 'tournaments/accueil.html')

def afficher_tournoi(request, tournoi_id):
    tournoi = Tournoi.objects.get(id=tournoi_id)
    matches = tournoi.matches.all()
    return render(request, 'accueil.html', {'tournoi': tournoi, 'matches': matches})

# Vue pour l'inscription d'un joueur à un tournoi
def inscrire_joueur(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi, pk=tournoi_id)
    
    if request.method == 'POST':
        # Récupérer le nom du joueur depuis le formulaire
        nom = request.POST.get('nom')
        if nom:
            # Créer un nouveau participant et l'ajouter au tournoi
            participant = Participant.objects.create(nom=nom)
            # Associer ce participant au tournoi, vous pouvez personnaliser cette logique
            # Cela dépend de comment vous gérez les joueurs et le tournoi.
            return HttpResponse(f'{participant.nom} a été inscrit au tournoi {tournoi.nom}')
        else:
            return HttpResponse('Erreur : Nom du joueur manquant.')
    
    # Afficher le formulaire d'inscription
    return render(request, 'inscrire_joueur.html', {'tournoi': tournoi})

def gerer_scores(request, tournoi_id):
    tournoi = get_object_or_404(Tournoi, pk=tournoi_id)
    matches = tournoi.matches.all()

    if request.method == 'POST':
        # Récupérer et mettre à jour les scores pour chaque match
        for match in matches:
            score_p1 = request.POST.get(f'score_participant1_{match.id}')
            score_p2 = request.POST.get(f'score_participant2_{match.id}')

            if score_p1 is not None:
                match.score_participant1 = int(score_p1)
            if score_p2 is not None:
                match.score_participant2 = int(score_p2)
            
            # Mise à jour du gagnant en fonction des scores
            if match.score_participant1 > match.score_participant2:
                match.gagnant = match.participant1
            elif match.score_participant2 > match.score_participant1:
                match.gagnant = match.participant2
            else:
                match.gagnant = None  # En cas d'égalité, pas de gagnant
            
            match.save()

        return render(request, 'scores_updated.html', {'tournoi': tournoi, 'matches': matches})

    return render(request, 'gerer_scores.html', {'tournoi': tournoi, 'matches': matches})