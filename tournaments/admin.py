from django.contrib import admin
from .models import Joueur, Match, Tournoi

class MatchAdmin(admin.ModelAdmin):
    list_display = ('participant1', 'participant2', 'score_participant1', 'score_participant2', 'gagnant', 'round', 'tournoi')
    fields = ('participant1', 'participant2', 'score_participant1', 'score_participant2', 'gagnant', 'round', 'tournoi')
    list_editable = ('score_participant1', 'score_participant2', 'gagnant',)

class TournoiAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date')

admin.site.register(Joueur)
admin.site.register(Match, MatchAdmin)
admin.site.register(Tournoi, TournoiAdmin)
