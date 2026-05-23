# Advent of Code 2025 - Day 7
# Rainfall Grid: Count Paths from S to the Bottom
#
# QUESTION:
# Grid contains: S (start), '.' (pass through), '|' (pass through), '^' (split), others (wall/stop).
# Rain falls downward from S. Movement rules:
#   '.' / 'S' / '|' → fall straight down (row + 1)
#   '^'             → split: go left AND right simultaneously
#   out of bounds   → counts as 1 completed path
#   anything else   → counts as 1 completed path (hits a wall)
#
# Part 1: Count the paths assuming '^' acts as a simple pass-through (fall straight down).
#         (The attempted grid-simulation approach below.)
# Part 2: Count total paths where '^' causes a real split into two branches.
#
# APPROACH (Part 2):
# Memoized recursion. At '^', the result is left_paths + right_paths.
# At any stopping condition, return 1.
# @cache handles repeated states efficiently.

from functools import cache
import sys

grid = sys.stdin.read().strip().splitlines()
grid = [list(line) for line in grid]

S = [(r, c)
     for r, row in enumerate(grid)
     for c, ch in enumerate(row)
     if ch == "S"][0]

# --- Part 1 attempt: simulate by propagating '|' markers row by row ---
# (this approach got complicated with edge cases — replaced by Part 2's recursion)
# a = [list(line) for line in open(0)]
# for n in range(len(a[0])):
#     if a[0][n] == 'S':
#         a[1][n] = '|'
#         break
# count = 0
# for l in range(1, len(a)-1):
#     for m in range(len(a[l])):
#         if a[l][m] == "|" and a[l+1][m] == "^":
#             count += 2
#             a[l+1][m-1] = '|'
#             a[l+1][m+1] = '|'
#         elif a[l][m] == "|" and a[l+1][m] != "^":
#             a[l+1][m] = '|'
# print(count)

# --- Part 2: clean memoized recursion ---
@cache
def solve(r, c):
    # fell off the bottom or sides → one completed path
    if r >= len(grid) or c < 0 or c >= len(grid[0]):
        return 1

    ch = grid[r][c]

    if ch in (".", "S", "|"):
        return solve(r + 1, c)  # keep falling straight down

    if ch == "^":
        return solve(r, c - 1) + solve(r, c + 1)  # split into two paths

    return 1  # hit a wall or unknown character — path ends here

print(solve(*S))
