document.addEventListener('DOMContentLoaded', function() {
    // Générer l'arbre de tournoi avec les données fournies par Django
    let data = {
        teams: teamsData, // Les équipes récupérées dans le template HTML
        results: [] // Si tu veux ajouter des résultats, tu peux les remplir ici
    };

    $('#tournoi').bracket({
        init: data,
        skipConsolationRound: true, // Si tu ne veux pas de match pour la 3ème place
    });
});
