# Advent of Code 2024 - Day 20: Race Condition
# Part 1 - Count cheats saving >= 100 picoseconds (cheat length 2)
#
# QUESTION:
# Grid maze with one path from S to E. The path has a known length.
# A "cheat" lets you pass through walls for exactly 2 steps.
# How many distinct cheats save at least 100 picoseconds?
# A cheat is identified by its (start, end) position pair.
#
# APPROACH:
# BFS from S to get distance from start to every position.
# BFS from E to get distance from every position to end.
# For every pair of positions exactly 2 steps apart (Manhattan),
# check if cheat_save = dist_s[a] + 2 + dist_e[b] < normal_dist.
# Count cheats where savings >= 100.

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
        if md == 2:
            saved = normal - (dist_s[(r1,c1)] + md + dist_e[(r2,c2)])
            if saved >= 100:
                count += 1

print(count)
