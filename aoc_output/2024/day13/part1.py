# Advent of Code 2024 - Day 13: Claw Contraption
# Part 1 - Minimum tokens to win as many prizes as possible
#
# QUESTION:
# Each claw machine has two buttons A and B:
#   Button A costs 3 tokens, moves claw by (ax, ay)
#   Button B costs 1 token,  moves claw by (bx, by)
# Prize is at position (px, py).
# You can press each button at most 100 times.
# Find how many tokens to win as many prizes as possible.
# If a prize is winnable, use the minimum tokens for it.
#
# Equation: a*ax + b*bx = px  and  a*ay + b*by = py
#           where 0 <= a, b <= 100
#
# APPROACH:
# Solve the 2x2 linear system using Cramer's rule.
# If the solution is integer and within 0-100, it's valid.

import sys
import re

blocks = sys.stdin.read().strip().split('\n\n')

total = 0

for block in blocks:
    nums = list(map(int, re.findall(r'\d+', block)))
    ax, ay, bx, by, px, py = nums

    # Cramer's rule: solve ax*a + bx*b = px, ay*a + by*b = py
    det = ax * by - ay * bx
    if det == 0:
        continue  # no unique solution

    a_num = px * by - py * bx
    b_num = ax * py - ay * px

    if a_num % det != 0 or b_num % det != 0:
        continue  # not an integer solution

    a = a_num // det
    b = b_num // det

    if 0 <= a <= 100 and 0 <= b <= 100:
        total += 3 * a + b  # A costs 3, B costs 1

print(total)
