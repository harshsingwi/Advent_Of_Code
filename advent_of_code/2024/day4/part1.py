# Advent of Code 2024 - Day 4: Ceres Search
# Part 1 - Find All Occurrences of "XMAS" in a Word Search
#
# QUESTION:
# You're given a grid of letters (a word search puzzle).
# Count how many times the word "XMAS" appears in the grid.
# It can appear horizontally, vertically, diagonally — forwards or backwards.
# Words can overlap each other.
#
# Example grid:
#   MMMSXXMASM
#   MSAMXMSMSA
#   AMXSXMAAMM
#   MSAMASMSMX
#   XMASAMXAMM
#   XXAMMXXAMA
#   SMSMSASXSS
#   SAXAMASAAA
#   MAMMMXMMMM
#   MXMXAXMASX
# Answer: 18
#
# APPROACH:
# For every cell in the grid that has 'X', try extending in all 8 directions
# and check if the next 3 characters spell out 'MAS'.
# If all 4 characters match XMAS, count it.

grid = [list(line.strip()) for line in open(0)]

ROWS = len(grid)
COLS = len(grid[0])
WORD = "XMAS"

# all 8 directions: (row_delta, col_delta)
directions = [
    (-1, -1),  # up-left diagonal
    (-1,  0),  # straight up
    (-1,  1),  # up-right diagonal
    ( 0, -1),  # straight left
    ( 0,  1),  # straight right
    ( 1, -1),  # down-left diagonal
    ( 1,  0),  # straight down
    ( 1,  1)   # down-right diagonal
]

def in_bounds(r, c):
    # make sure we don't fall off the grid
    return 0 <= r < ROWS and 0 <= c < COLS

count = 0

for r in range(ROWS):
    for c in range(COLS):

        # only start searching from cells with 'X' (first letter of XMAS)
        if grid[r][c] != 'X':
            continue

        for dr, dc in directions:
            rr, cc = r, c
            matched = True

            # check each character of XMAS one by one in this direction
            for k in range(len(WORD)):
                if not in_bounds(rr, cc) or grid[rr][cc] != WORD[k]:
                    matched = False
                    break
                rr += dr
                cc += dc

            if matched:
                count += 1

print(count)
