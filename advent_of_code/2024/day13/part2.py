# Advent of Code 2024 - Day 13: Claw Contraption
# Part 2 - Same but prize positions are 10000000000000 further away
#
# QUESTION:
# Same machines as Part 1, but add 10000000000000 to both px and py.
# The 100-press limit no longer applies.
# Find minimum tokens to win all winnable prizes.
#
# APPROACH:
# Same Cramer's rule — just remove the 0-100 bound check.
# The huge offset makes brute force impossible but the math is the same.

import sys
import re

blocks = sys.stdin.read().strip().split('\n\n')

OFFSET = 10000000000000
total = 0

for block in blocks:
    nums = list(map(int, re.findall(r'\d+', block)))
    ax, ay, bx, by, px, py = nums
    px += OFFSET
    py += OFFSET

    det = ax * by - ay * bx
    if det == 0:
        continue

    a_num = px * by - py * bx
    b_num = ax * py - ay * px

    if a_num % det != 0 or b_num % det != 0:
        continue  # no integer solution

    a = a_num // det
    b = b_num // det

    if a >= 0 and b >= 0:
        total += 3 * a + b

print(total)
