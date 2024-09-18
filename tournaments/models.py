from django.db import models

class Participant(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Match(models.Model):
    participant1 = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='match_participant1')
    participant2 = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='match_participant2')
    score_participant1 = models.IntegerField(default=0)
    score_participant2 = models.IntegerField(default=0)
    gagnant = models.ForeignKey(Participant, on_delete=models.SET_NULL, null=True, blank=True, related_name='match_gagnant')

    def __str__(self):
        return f"{self.participant1} vs {self.participant2}"

class Tournoi(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateField()
    matches = models.ManyToManyField(Match)

    def __str__(self):
        return self.nom
