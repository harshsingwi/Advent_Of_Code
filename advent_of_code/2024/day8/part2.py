# Advent of Code 2024 - Day 8: Resonant Collinearity
# Part 2 - Antinodes extend infinitely along the line through each pair
#
# QUESTION:
# Same grid and same antenna setup as Part 1.
# Now antinodes appear at EVERY grid position that lies on the line through
# any pair of same-frequency antennas — including the antenna positions themselves.
# There's no distance limit anymore — extend in both directions until out of bounds.
#
# Count unique antinode positions.
#
# APPROACH:
# For each pair, compute the direction vector (dr, dc) between them.
# Then walk in both directions from one antenna, adding every in-bounds position.

import sys
from collections import defaultdict
from math import gcd

grid = sys.stdin.read().splitlines()
ROWS, COLS = len(grid), len(grid[0])

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

            # reduce the step to smallest integer vector on this line
            dr, dc = r2 - r1, c2 - c1
            g = gcd(abs(dr), abs(dc))
            dr, dc = dr // g, dc // g

            # walk in the positive direction from (r1,c1)
            r, c = r1, c1
            while 0 <= r < ROWS and 0 <= c < COLS:
                antinodes.add((r, c))
                r += dr
                c += dc

            # walk in the negative direction from (r1,c1)
            r, c = r1 - dr, c1 - dc
            while 0 <= r < ROWS and 0 <= c < COLS:
                antinodes.add((r, c))
                r -= dr
                c -= dc

print(len(antinodes))
