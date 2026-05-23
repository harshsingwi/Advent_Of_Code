# Advent of Code 2024 - Day 20: Race Condition
# Part 2 - Count cheats saving >= 100 picoseconds (cheat length up to 20)
#
# QUESTION:
# Same maze as Part 1.
# Now cheats can last up to 20 picoseconds (pass through walls for up to 20 steps).
# The cost of the cheat = Manhattan distance between start and end of cheat.
# Count cheats where time saved >= 100.
#
# APPROACH:
# Same idea as Part 1 — for each pair of track positions within Manhattan distance 20,
# check if the cheat (direct path between them) saves >= 100 steps.

import sys
from collections import deque

grid = sys.stdin.read().splitlines()
ROWS, COLS = len(grid), len(grid[0])
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

S = next((r,c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 'S')
E = next((r,c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 'E')

def bfs(start):
    dist = {start: 0}
    q = deque([start])
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in dist and grid[nr][nc] != '#':
                dist[(nr,nc)] = dist[(r,c)] + 1
                q.append((nr,nc))
    return dist

dist_s = bfs(S)
dist_e = bfs(E)
normal = dist_s[E]
track = [pos for pos in dist_s if pos in dist_e]

count = 0
for r1, c1 in track:
    for r2, c2 in track:
        md = abs(r1-r2) + abs(c1-c2)
        if md <= 20:  # cheat can be up to 20 steps
            saved = normal - (dist_s[(r1,c1)] + md + dist_e[(r2,c2)])
            if saved >= 100:
                count += 1

print(count)
