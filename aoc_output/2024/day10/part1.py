# Advent of Code 2024 - Day 10: Hoof It
# Part 1 - Count reachable 9s from each trailhead (score)
#
# QUESTION:
# The grid contains digits 0-9 representing heights.
# A "trailhead" is any cell with height 0.
# A valid hiking trail starts at a 0 and increases by exactly 1 at each step
# (no diagonals — only up/down/left/right).
# The "score" of a trailhead = how many distinct height-9 cells it can reach.
# Return the sum of all trailhead scores.
#
# APPROACH:
# BFS/DFS from each 0 cell, only stepping to adjacent cells with height = current+1.
# Collect all reachable 9s in a set (distinct count).

import sys
from collections import deque

grid = [list(map(int, line)) for line in sys.stdin.read().splitlines()]
ROWS, COLS = len(grid), len(grid[0])
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def score(sr, sc):
    # BFS to find all reachable 9s from trailhead at (sr, sc)
    reachable = set()
    q = deque([(sr, sc)])
    visited = {(sr, sc)}
    while q:
        r, c = q.popleft()
        if grid[r][c] == 9:
            reachable.add((r, c))
            continue
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                if grid[nr][nc] == grid[r][c] + 1:
                    visited.add((nr, nc))
                    q.append((nr, nc))
    return len(reachable)

total = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 0:
            total += score(r, c)

print(total)
