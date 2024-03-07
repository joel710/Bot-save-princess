def nextMove(n, r, c, grid):
    # Trouver la position de la princesse
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                princess_r, princess_c = i, j
                break

    # Calculer la direction pour se dplacer
    if r < princess_r:
        return 'DOWN'
    elif r > princess_r:
        return 'UP'
    elif c < princess_c:
        return 'RIGHT'
    elif c > princess_c:
        return 'LEFT'
    return None

# Lire l'entre
n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for _ in range(n):
    grid.append(input())

# Afficher le mouvement suivant
print(nextMove(n, r, c, grid))
