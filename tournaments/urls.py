from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('inscrire/<int:tournoi_id>/', views.inscrire_joueur, name='inscrire_joueur'),
    path('scores/<int:tournoi_id>/', views.gerer_scores, name='gerer_scores'),
    
]