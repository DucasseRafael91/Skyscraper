#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def calcul_increase(sequence):
    """
    Permet de générer les bordures de la grille
    :param sequence: liste de valeurs de la grille (bordure gauche ou haute )
    :return: valeur à placer dans la bordure gauche ou haute
    """
    count = 1
    max_seen = sequence[0]
    for val in sequence[1:]:
        if val > max_seen:
            count += 1
            max_seen = val
    return count

def calcul_increase_reverse(sequence):
    """
    Permet de générer les bordures de la grille
    :param sequence: liste de valeurs de la grille (bordure droite ou basse )
    :return: valeur à placer dans la bordure droite ou basse dans la grille
    """
    return calcul_increase(sequence[::-1])

def print_matrice(grid):
    """
    Permet l'affichage de la grille.
    :param grid: Grille à afficher
    :return: False si erreur ou sinon al grille
    """
    for row in grid:
        print(" ".join(str(cell).rjust(2) for cell in row))

def create_game_grid(size):
    grid = [[0 for _ in range(size)] for _ in range(size)]

    def is_valid(row, col, val):
        return val not in grid[row] and all(grid[r][col] != val for r in range(size))

    def fill(row, col):
        if row == size:
            return True
        next_row, next_col = (row, col + 1) if col + 1 < size else (row + 1, 0)

        values = list(range(1, size + 1))
        random.shuffle(values)
        for val in values:
            if is_valid(row, col, val):
                grid[row][col] = val
                if fill(next_row, next_col):
                    return True
                grid[row][col] = 0
        return False

    fill(0, 0)
    return grid

def add_borders(game_grid):
    """
    Permet d'ajouter les bordures de la grille à la zone de jeu.
    :param game_grid: Zone de jeu
    :return: Retourne la brille avec les bordures ajoutées
    """
    size = len(game_grid)
    grid = [['X'] + [' ' for _ in range(size)] + ['X']]
    for row in game_grid:
        grid.append([' '] + row + [' '])  # middle rows with side borders
    grid.append(['X'] + [' ' for _ in range(size)] + ['X'])  # bottom border
    return grid

def fill_borders(grid):
    """
    Permet de remplacer les valeurs X dans les borudres par les vraies valeurs
    :param grid: Grille de jeu avec les bordures
    :return: None
    """
    size = len(grid) - 2
    for i in range(1, size + 1):
        row_vals = grid[i][1:-1]
        grid[i][0] = calcul_increase(row_vals)
        grid[i][-1] = calcul_increase_reverse(row_vals)

        col_vals = [grid[r][i] for r in range(1, size + 1)]
        grid[0][i] = calcul_increase(col_vals)
        grid[-1][i] = calcul_increase_reverse(col_vals)

def hide_game_zone(grid, symbol):
    """
    Permet de remplacer les valeurs de la zone de jeu par un symbole voulue (X par défaut )
    :param grid: Grille de jeu avec les bordures
    :param symbol: symbole qui va remplacer les valeurs de la zone de jeu
    :return: None
    """
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid) - 1):
            grid[i][j] = symbol

def main():
    while True:
        user_input = input("Entrez la taille de la grille (4 à 8) : ")
        if user_input.isdigit():
            size = int(user_input)
            if 4 <= size <= 50:
                game_grid = create_game_grid(size)
                full_grid = add_borders(game_grid)
                fill_borders(full_grid)

                print("\n GRILLE SOLUTION :\n")
                print_matrice(full_grid)

                hide_game_zone(full_grid, "X")

                print("\n PUZZLE À RÉSOUDRE :\n")
                print_matrice(full_grid)
                break
            else:
                print("Erreur : nombre hors limites.")
        else:
            print("Erreur : entrez un nombre entier.")
            continue

if __name__ == '__main__':
    main()
