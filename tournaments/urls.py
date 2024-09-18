from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('tournoi/<int:tournoi_id>/inscrire/', views.inscrire_joueur, name='inscrire_joueur'),
    path('tournoi/<int:tournoi_id>/bracket/', views.tournoi_bracket, name='tournoi_bracket'),
    path('tournoi/<int:tournoi_id>/', views.afficher_tournoi, name='afficher_tournoi'), 
]