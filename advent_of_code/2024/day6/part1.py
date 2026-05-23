# Advent of Code 2024 - Day 6: Guard Gallivant
# Part 1 - Count distinct positions visited by the guard
#
# QUESTION:
# A guard patrols a lab following strict rules. The grid has obstacles '#'
# and the guard starts at '^' facing up.
# Movement rules:
#   - If there's an obstacle directly ahead, turn RIGHT 90 degrees
#   - Otherwise, move one step forward
#   - Guard leaves the grid when they step out of bounds
#
# Count how many distinct positions the guard visits (including the start).
#
# APPROACH:
# Simulate the guard's movement. Track visited positions in a set.
# Turn right means: up→right→down→left→up (cycle through direction list).

import sys

grid = [list(line) for line in sys.stdin.read().splitlines()]
ROWS, COLS = len(grid), len(grid[0])

# find starting position
r, c = next((r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == '^')

# directions: up, right, down, left — turning right cycles through these
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 0  # start facing up

visited = set()
visited.add((r, c))

while True:
    dr, dc = dirs[d]
    nr, nc = r + dr, c + dc

    if not (0 <= nr < ROWS and 0 <= nc < COLS):
        break  # guard walks off the grid

    if grid[nr][nc] == '#':
        d = (d + 1) % 4  # obstacle ahead — turn right
    else:
        r, c = nr, nc  # step forward
        visited.add((r, c))

print(len(visited))
