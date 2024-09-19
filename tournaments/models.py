from django.db import models

class Joueur(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Tournoi(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.nom

class Match(models.Model):
    participant1 = models.ForeignKey(Joueur, on_delete=models.CASCADE, related_name='match_participant1')
    participant2 = models.ForeignKey(Joueur, on_delete=models.CASCADE, related_name='match_participant2')
    score_participant1 = models.IntegerField(default=0)
    score_participant2 = models.IntegerField(default=0)
    gagnant = models.ForeignKey(Joueur, on_delete=models.SET_NULL, null=True, blank=True, related_name='match_gagnant')
    tournoi = models.ForeignKey(Tournoi, on_delete=models.CASCADE, related_name='matches_in_tournoi')

    round = models.CharField(max_length=20, choices=[
        ('Quart de finale', 'Quart de finale'),
        ('Demi-finale', 'Demi-finale'),
        ('Finale', 'Finale'),
    ], default='Quart de finale')

    def __str__(self):
        return f"{self.participant1} vs {self.participant2} ({self.round})"

    def mettre_a_jour_gagnant(self):
        """Met à jour automatiquement le gagnant en fonction des scores."""
        if self.score_participant1 > self.score_participant2:
            self.gagnant = self.participant1
        elif self.score_participant2 > self.score_participant1:
            self.gagnant = self.participant2
        else:
            self.gagnant = None  # S'il y a égalité
        self.save()

