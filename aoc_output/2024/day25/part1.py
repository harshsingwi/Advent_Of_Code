# Advent of Code 2024 - Day 25: Code Chronicle
# Part 1 - Count lock/key pairs that fit together
#
# QUESTION:
# The input contains schematics for locks and keys (5 columns, 7 rows each).
# Locks: top row is '#####', filled from top down → pin heights are columns of '#'
# Keys:  bottom row is '#####', filled from bottom up → pin heights are columns of '#'
#
# A lock and key FIT if for every column, lock_height + key_height <= 5
# (they don't overlap when the key is inserted into the lock).
#
# Count the number of lock/key pairs that fit.
#
# APPROACH:
# Parse each schematic into column heights (count '#' per column, minus 1 for the border).
# Separate into locks (top row full) and keys (bottom row full).
# Try every lock/key combination and check the fit condition.

import sys

blocks = sys.stdin.read().strip().split('\n\n')

locks = []
keys = []

for block in blocks:
    rows = block.splitlines()
    # count '#' in each of the 5 columns (excluding the solid top/bottom row)
    heights = [sum(1 for r in rows[1:6] if r[c] == '#') for c in range(5)]
    if rows[0] == '#####':
        locks.append(heights)  # top is solid → it's a lock
    else:
        keys.append(heights)   # bottom is solid → it's a key

count = 0
for lock in locks:
    for key in keys:
        # they fit if no column overlaps (total height <= 5 in every column)
        if all(l + k <= 5 for l, k in zip(lock, key)):
            count += 1

print(count)
