# Advent of Code 2025 - Day 4
# Cellular Automaton: '@' Cells Removed by Neighbor Count
#
# QUESTION:
# Grid of '.' and '@'. Cells are removed in rounds based on their '@' neighbor count.
#
# Part 1: Remove '@' cells with fewer than 2 '@' neighbors each round.
#         Count total removed until stable.
# Part 2: Remove '@' cells with fewer than 4 '@' neighbors each round.
#         Count total removed until stable.
#
# Neighbors = all 8 surrounding cells (including diagonals).
# Removal is simultaneous per round — not sequential.

a = []
while True:
    b = input().strip()
    if not b:
        break
    a.append(list(b))

import copy

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

def count_adj(grid, i, j):
    adj = 0
    rows, cols = len(grid), len(grid[0])
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == '@':
            adj += 1
    return adj

def simulate(grid, threshold):
    # run until stable, return total cells removed
    grid = copy.deepcopy(grid)
    total_removed = 0
    while True:
        rows, cols = len(grid), len(grid[0])
        to_remove = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@' and count_adj(grid, i, j) < threshold:
                    to_remove.append((i, j))
        if not to_remove:
            break
        for i, j in to_remove:
            grid[i][j] = '.'
        total_removed += len(to_remove)
    return total_removed

# Part 1: threshold = 2 neighbors
# print(simulate(a, 2))

# Part 2: threshold = 4 neighbors
print(simulate(a, 4))
