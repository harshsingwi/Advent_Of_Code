# Advent of Code 2024 - Day 18: RAM Run
# Part 1 - Shortest path after first 1024 bytes fall
#
# QUESTION:
# Bytes fall one by one into a 71x71 grid (0 to 70) and become walls '#'.
# You start at (0,0) and need to reach (70,70).
# After the first 1024 bytes have fallen, find the minimum number of steps
# to reach the exit. Move only up/down/left/right, not through walls.
#
# APPROACH:
# BFS from (0,0) to (70,70) on the grid with first 1024 walls placed.

import sys
from collections import deque

coords = [tuple(map(int, line.split(','))) for line in sys.stdin.read().splitlines()]

SIZE = 70
blocked = set(coords[:1024])

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
q = deque([(0, 0, 0)])  # (steps, row, col)
visited = {(0, 0)}

while q:
    steps, r, c = q.popleft()
    if r == SIZE and c == SIZE:
        print(steps)
        break
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr <= SIZE and 0 <= nc <= SIZE and (nr, nc) not in visited and (nc, nr) not in blocked:
            visited.add((nr, nc))
            q.append((steps + 1, nr, nc))
