document.addEventListener('DOMContentLoaded', function () {
    // Vérifie que les données sont bien récupérées
    console.log("Teams Quart de finale:", teamsData);
    console.log("Teams Demi-finale:", demiFinaleData);
    console.log("Teams Finale:", finaleData);
    console.log("Champion Data:", championData);
    console.log("Results Data:", resultsData);

    // Crée un élément de tournoi sans jQuery
    const tournoiContainer = document.getElementById('tournoi');
    if (!tournoiContainer) {
        console.error("Élément #tournoi introuvable");
        return;
    }

    // Fonction pour créer un élément d'équipe
    function createTeamElement(name) {
        const teamElement = document.createElement('div');
        teamElement.classList.add('team');
        teamElement.textContent = name;
        return teamElement;
    }

    // Fonction pour créer un match dans le bracket
    function createMatch(team1, team2) {
        const matchElement = document.createElement('div');
        matchElement.classList.add('match');
        matchElement.appendChild(createTeamElement(team1));
        matchElement.appendChild(createTeamElement(team2));
        return matchElement;
    }

    // Fonction pour générer un round
    function createRound(matches) {
        const roundElement = document.createElement('div');
        roundElement.classList.add('round');
        matches.forEach(match => {
            roundElement.appendChild(createMatch(match[0], match[1]));
        });
        return roundElement;
    }

    // Ajoute les rounds au bracket
    tournoiContainer.appendChild(createRound(teamsData));  // Quart de finale
    tournoiContainer.appendChild(createRound(demiFinaleData));  // Demi-finale
    tournoiContainer.appendChild(createRound(finaleData));  // Finale

    // Ajoute le champion
    const championMatch = createMatch(championData[0][0], championData[0][1]);
    const championRound = document.createElement('div');
    championRound.classList.add('round');
    championRound.appendChild(championMatch);
    tournoiContainer.appendChild(championRound);
});
