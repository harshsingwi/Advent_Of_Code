# Advent of Code 2025 - Day 10
# Flood Fill: Count Enclosed Regions in a Grid
#
# QUESTION:
# You're given a grid of '.' (empty) and '#' (walls).
# A region is a group of connected '.' cells (4-directional, no diagonals).
# Cells on the border of the grid are considered "open" (connected to outside).
#
# Part 1: Count how many '.' regions touch the border (are reachable from outside).
# Part 2: Count how many '.' cells are completely enclosed
#         (not reachable from the border at all).
#
# APPROACH:
# Flood fill from all border '.' cells to mark what's "outside".
# Any '.' cell not reached by that flood fill is enclosed.
# Part 1 = number of distinct connected components touching the border.
# Part 2 = count of all unreached '.' cells.

import sys
from collections import deque

grid = sys.stdin.read().splitlines()
ROWS, COLS = len(grid), len(grid[0])
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

# flood fill outward from all border '.' cells
outside = set()
q = deque()

for r in range(ROWS):
    for c in range(COLS):
        if (r == 0 or r == ROWS-1 or c == 0 or c == COLS-1) and grid[r][c] == '.':
            if (r, c) not in outside:
                outside.add((r, c))
                q.append((r, c))

while q:
    r, c = q.popleft()
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in outside and grid[nr][nc] == '.':
            outside.add((nr, nc))
            q.append((nr, nc))

# Part 1: count connected components that touch the border
# (each flood fill from a new unvisited border cell = one open region)
visited_components = set()
border_cells = [(r, c) for r in range(ROWS) for c in range(COLS)
                if (r == 0 or r == ROWS-1 or c == 0 or c == COLS-1) and grid[r][c] == '.']

seen = set()
open_regions = 0
for start in border_cells:
    if start not in seen:
        open_regions += 1
        bq = deque([start])
        seen.add(start)
        while bq:
            r, c = bq.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (nr, nc) in outside and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    bq.append((nr, nc))

# print(open_regions)   # Part 1

# Part 2: count enclosed '.' cells (not reachable from border)
enclosed = sum(
    1 for r in range(ROWS) for c in range(COLS)
    if grid[r][c] == '.' and (r, c) not in outside
)
print(enclosed)
