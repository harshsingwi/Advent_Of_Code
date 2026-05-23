# Advent of Code 2024 - Day 8: Resonant Collinearity
# Part 1 - Count unique antinode positions
#
# QUESTION:
# The grid contains antennas, each marked with a letter or digit.
# Antennas of the same frequency can create "antinodes".
# For any two antennas A and B of the same frequency, antinodes appear at:
#   - The point that is twice as far from B as from A (on A's side)
#   - The point that is twice as far from A as from B (on B's side)
# Mathematically: if A=(r1,c1) and B=(r2,c2), antinodes are at:
#   (2*r1 - r2, 2*c1 - c2) and (2*r2 - r1, 2*c2 - c1)
#
# Count how many unique positions within the grid contain at least one antinode.
#
# APPROACH:
# Group antenna positions by frequency. For each pair of same-frequency antennas,
# compute both antinode positions. Collect all in-bounds ones in a set.

import sys
from collections import defaultdict

grid = sys.stdin.read().splitlines()
ROWS, COLS = len(grid), len(grid[0])

# group antenna positions by their frequency character
antennas = defaultdict(list)
for r in range(ROWS):
    for c in range(COLS):
        ch = grid[r][c]
        if ch != '.':
            antennas[ch].append((r, c))

antinodes = set()

for freq, positions in antennas.items():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            r1, c1 = positions[i]
            r2, c2 = positions[j]
            # antinode on the far side of antenna 1
            ar1, ac1 = 2 * r1 - r2, 2 * c1 - c2
            # antinode on the far side of antenna 2
            ar2, ac2 = 2 * r2 - r1, 2 * c2 - c1

            if 0 <= ar1 < ROWS and 0 <= ac1 < COLS:
                antinodes.add((ar1, ac1))
            if 0 <= ar2 < ROWS and 0 <= ac2 < COLS:
                antinodes.add((ar2, ac2))

print(len(antinodes))
