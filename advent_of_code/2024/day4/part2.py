# Advent of Code 2024 - Day 4: Ceres Search
# Part 2 - Find X-MAS Patterns (Two MAS crossing in an X shape)
#
# QUESTION:
# Now you need to find a different pattern: two "MAS" words forming an X shape.
# Each "MAS" goes diagonally, and they cross at the 'A' in the middle.
# The two MAS words can be forwards (MAS) or backwards (SAM) — both count.
#
# Visual example (one X-MAS pattern):
#   M . S
#   . A .
#   M . S
#
# Another valid one:
#   S . M
#   . A .
#   S . M
#
# Basically: center must be 'A', and both diagonals must spell MAS or SAM.
#
# APPROACH:
# Scan every 'A' in the grid (it must be the center of the X).
# Check both diagonals (top-left to bottom-right, and top-right to bottom-left).
# Each diagonal must form "MAS" or "SAM" (i.e., one end is M and other is S).

grid = [list(line.strip()) for line in open(0)]

ROWS = len(grid)
COLS = len(grid[0])

def in_bounds(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS

count = 0

for r in range(ROWS):
    for c in range(COLS):

        # center of the X must be 'A'
        if grid[r][c] != 'A':
            continue

        # diagonal 1: top-left → center → bottom-right
        diag1 = [(r - 1, c - 1), (r, c), (r + 1, c + 1)]
        # diagonal 2: top-right → center → bottom-left
        diag2 = [(r - 1, c + 1), (r, c), (r + 1, c - 1)]

        # all 6 positions must be inside the grid
        if not all(in_bounds(x, y) for x, y in diag1 + diag2):
            continue

        # build the string for each diagonal
        s1 = "".join(grid[x][y] for x, y in diag1)
        s2 = "".join(grid[x][y] for x, y in diag2)

        # each diagonal must read MAS or SAM (i.e., M and S on opposite ends)
        if s1 in ("MAS", "SAM") and s2 in ("MAS", "SAM"):
            count += 1

print(count)
