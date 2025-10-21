Gratte-Ciel (Skyscrapers)

Gratte-Ciel est un jeu de logique inspiré du puzzle "Skyscrapers" présenté régulièrement aux Championnats du monde de jeux de logique. Ce projet Python propose un générateur, un affichage et un solveur automatique de grilles de jeu de 4×4 à 8×8.

🔍 Présentation

Le jeu du gratte-ciel se joue sur une grille carrée où chaque case contient un immeuble de hauteur unique par ligne et colonne. Les indices placés autour de la grille indiquent combien d’immeubles sont visibles depuis ce point de vue, en tenant compte du fait que les immeubles plus hauts cachent les plus petits derrière eux.

Ce projet propose :

🧱 La génération d'une grille solution valide

👁️ Le calcul des indices visibles (création de la grille problème)

🧠 Un solveur automatique basé sur des stratégies humaines

🎛️ Une interface console interactive

🚀 Fonctionnalités

✅ Génération aléatoire d'une grille solution de taille 4×4 à 8×8

✅ Calcul automatique des indices extérieurs pour générer une grille problème

✅ Résolution automatique de la grille problème sans force brute : le solveur applique des techniques de déduction similaires à celles utilisées par les joueurs humains

✅ Affichage clair de la grille dans le terminal

🧠 Stratégie de résolution

Le solveur repose sur une suite de règles inspirées de la logique humaine :

Remplissage direct : si un indice est égal à la taille de la grille, la ligne/colonne est forcément en ordre croissant.

Blocages croisés : en croisant les contraintes des lignes et des colonnes, on élimine les possibilités impossibles.

Propagation logique : les placements certains permettent d'en déduire d'autres par élimination.

Backtracking minimal : utilisé uniquement en dernier recours quand plusieurs configurations restent possibles.

L’approche est systématique et permet de résoudre des grilles de difficulté moyenne à élevée sans recherche exhaustive.

🎮 Utilisation

Au lancement, vous serez invité à entrer la taille de la grille (entre 4 et 8). Le programme générera alors :

une grille solution (en interne),

les indices visibles depuis chaque bord,

et vous proposera de résoudre automatiquement la grille ou de tenter vous-même.


📚 Technologies utilisées

Python 3.13

Aucune dépendance externe 

✅ Avancement

 Générateur de grille solution

 Générateur d’indices visibles

 Affichage console

 Solveur automatique logique

 Interface interactive simple

 Interface graphique (prévue dans une prochaine version)