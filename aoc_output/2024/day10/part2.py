# Advent of Code 2024 - Day 10: Hoof It
# Part 2 - Count distinct hiking trails from each trailhead (rating)
#
# QUESTION:
# Same grid as Part 1.
# Now instead of counting distinct 9-cells reachable, count distinct
# PATHS from each trailhead to any 9. Each unique sequence of steps counts separately.
# The "rating" of a trailhead = number of distinct trails from it.
# Return the sum of all trailhead ratings.
#
# APPROACH:
# DFS with memoization. dp[r][c] = number of distinct trails from (r,c) to any 9.
# Base case: if height is 9, there's exactly 1 trail (the trivial one ending here).
# Recursive: sum up dp values of all valid neighbors (height = current+1).

import sys
from functools import lru_cache

grid = [list(map(int, line)) for line in sys.stdin.read().splitlines()]
ROWS, COLS = len(grid), len(grid[0])
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

@lru_cache(maxsize=None)
def count_trails(r, c):
    if grid[r][c] == 9:
        return 1  # reached the summit — this is one complete trail
    total = 0
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            if grid[nr][nc] == grid[r][c] + 1:
                total += count_trails(nr, nc)
    return total

result = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 0:
            result += count_trails(r, c)

print(result)
