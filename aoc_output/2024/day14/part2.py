# Advent of Code 2024 - Day 14: Restroom Redoubt
# Part 2 - Find the Easter egg: when do robots form a Christmas tree?
#
# QUESTION:
# Same robots and grid.
# At some specific second, the robots arrange themselves into a Christmas tree shape.
# Find that second.
#
# APPROACH:
# The Christmas tree will have robots clustered together unusually tightly.
# Heuristic: find the second where the robots have the minimum variance in position
# (i.e. they're most clustered together).
# Due to Chinese Remainder Theorem, we only need to check up to WIDTH*HEIGHT seconds.

import sys
import re

WIDTH, HEIGHT = 101, 103
lines = sys.stdin.read().splitlines()

robots = []
for line in lines:
    px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
    robots.append((px, py, vx, vy))

def variance(positions):
    xs = [p[0] for p in positions]
    ys = [p[1] for p in positions]
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    return sum((x - mx)**2 + (y - my)**2 for x, y in positions)

min_var = float('inf')
best_t = 0

for t in range(WIDTH * HEIGHT):
    positions = [((px + vx*t) % WIDTH, (py + vy*t) % HEIGHT)
                 for px, py, vx, vy in robots]
    v = variance(positions)
    if v < min_var:
        min_var = v
        best_t = t

print(best_t)
