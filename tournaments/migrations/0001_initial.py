# Generated by Django 5.1.1 on 2024-09-17 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Joueur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Tournoi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_joueur1', models.IntegerField(blank=True, null=True)),
                ('score_joueur2', models.IntegerField(blank=True, null=True)),
                ('date_match', models.DateField()),
                ('joueur1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joueur1', to='tournaments.joueur')),
                ('joueur2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joueur2', to='tournaments.joueur')),
                ('tournoi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournoi')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_inscription', models.DateField(auto_now_add=True)),
                ('joueur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.joueur')),
                ('tournoi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournoi')),
            ],
        ),
    ]
