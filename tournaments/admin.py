from django.contrib import admin
from .models import Participant, Match, Tournoi

class MatchAdmin(admin.ModelAdmin):
    list_display = ('participant1', 'participant2', 'score_participant1', 'score_participant2', 'gagnant')
    fields = ('participant1', 'participant2', 'score_participant1', 'score_participant2', 'gagnant')
    list_editable = ('score_participant1', 'score_participant2', 'gagnant')

class TournoiAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date')
    filter_horizontal = ('matches',)

admin.site.register(Participant)
admin.site.register(Match, MatchAdmin)
admin.site.register(Tournoi, TournoiAdmin)
