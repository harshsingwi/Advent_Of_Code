# Advent of Code 2024 - Day 16: Reindeer Maze
# Part 1 - Lowest score to reach the end of the maze
#
# QUESTION:
# Grid maze with S (start, facing East) and E (end), walls '#', empty '.'.
# Reindeer can:
#   - Move forward 1 step: costs 1 point
#   - Turn 90 degrees left or right: costs 1000 points
# Find the lowest possible score to get from S to E.
#
# APPROACH:
# Dijkstra's algorithm. State = (row, col, direction).
# Direction is 0=East, 1=South, 2=West, 3=North (turning adds 1000).

import sys
import heapq

grid = sys.stdin.read().splitlines()
ROWS, COLS = len(grid), len(grid[0])

# find start S and end E
S = next((r,c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 'S')
E = next((r,c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 'E')

# directions: East=0, South=1, West=2, North=3
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# Dijkstra: (cost, row, col, direction)
heap = [(0, S[0], S[1], 0)]  # start facing East
dist = {}

while heap:
    cost, r, c, d = heapq.heappop(heap)
    if (r, c, d) in dist:
        continue
    dist[(r, c, d)] = cost

    if (r, c) == E:
        print(cost)
        break

    # move forward
    nr, nc = r + dr[d], c + dc[d]
    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != '#':
        if (nr, nc, d) not in dist:
            heapq.heappush(heap, (cost + 1, nr, nc, d))

    # turn left or right (no movement, just turn)
    for turn in [-1, 1]:
        nd = (d + turn) % 4
        if (r, c, nd) not in dist:
            heapq.heappush(heap, (cost + 1000, r, c, nd))
