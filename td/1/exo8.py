def check_word(grid, mot):
    ligne = len(grid)
    colonne = len(grid[0])

    for ligne in grid:
        if mot in ''.join(ligne):
            return True
    
    for colonne in range(grid):
        colonne_mot = ''.join(grid[lignes][colonne] for lignes in range(ligne))
        if mot in colonne_mot:
            return True
    return False

grid = [['C', 'A', 'T'],['D', 'O', 'G'],['R', 'A', 'T']]
mot = "DOG"
print(check_word(grid, mot))