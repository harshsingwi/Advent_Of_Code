# Advent of Code 2024 - Day 6: Guard Gallivant
# Part 2 - Count positions where adding one obstacle creates a loop
#
# QUESTION:
# Same grid as Part 1.
# How many positions could you place a single new obstacle ('#') such that
# the guard gets stuck in an infinite loop?
# You can only place it on empty cells ('.'), not on the guard's start.
#
# APPROACH:
# For each cell the guard visits in Part 1 (candidate obstacle positions),
# simulate the guard's walk with that obstacle added.
# A loop is detected when the guard reaches a state (position + direction)
# it has already been in. If the guard loops → count it.
# Only test positions from the Part 1 visited set to avoid brute-forcing the whole grid.

import sys

grid = [list(line) for line in sys.stdin.read().splitlines()]
ROWS, COLS = len(grid), len(grid[0])

start_r, start_c = next((r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == '^')

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_visited(grid, sr, sc):
    # simulate and return all visited positions (for finding candidates)
    r, c, d = sr, sc, 0
    visited = set()
    visited.add((r, c))
    while True:
        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < ROWS and 0 <= nc < COLS):
            break
        if grid[nr][nc] == '#':
            d = (d + 1) % 4
        else:
            r, c = nr, nc
            visited.add((r, c))
    return visited

def causes_loop(grid, sr, sc, obs_r, obs_c):
    # simulate with extra obstacle at obs_r, obs_c — returns True if it loops
    r, c, d = sr, sc, 0
    seen_states = set()
    while True:
        state = (r, c, d)
        if state in seen_states:
            return True  # been here facing same direction — it's a loop
        seen_states.add(state)
        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < ROWS and 0 <= nc < COLS):
            return False  # walked off the grid — no loop
        if grid[nr][nc] == '#' or (nr == obs_r and nc == obs_c):
            d = (d + 1) % 4  # hit obstacle (real or new) — turn right
        else:
            r, c = nr, nc

# only test positions the guard actually visits (saves a lot of time)
candidates = get_visited(grid, start_r, start_c)
candidates.discard((start_r, start_c))  # can't place obstacle at start

count = 0
for (or_, oc) in candidates:
    if grid[or_][oc] == '.' and causes_loop(grid, start_r, start_c, or_, oc):
        count += 1

print(count)
