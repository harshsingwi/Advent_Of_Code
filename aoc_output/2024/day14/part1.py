# Advent of Code 2024 - Day 14: Restroom Redoubt
# Part 1 - Safety factor after 100 seconds
#
# QUESTION:
# Robots move in a grid (width=101, height=103) with wraparound.
# Each robot has a position (px, py) and velocity (vx, vy).
# After exactly 100 seconds, each robot is at:
#   final_x = (px + vx*100) % WIDTH
#   final_y = (py + vy*100) % HEIGHT
#
# Ignore robots on the exact middle row or column.
# Count robots in each of the 4 quadrants.
# Safety factor = product of the four quadrant counts.
#
# APPROACH:
# Compute final positions with modular arithmetic. Bin by quadrant.

import sys
import re
from math import prod

WIDTH, HEIGHT = 101, 103
lines = sys.stdin.read().splitlines()

robots = []
for line in lines:
    px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
    robots.append((px, py, vx, vy))

mid_x = WIDTH // 2
mid_y = HEIGHT // 2
quadrants = [0, 0, 0, 0]

for px, py, vx, vy in robots:
    fx = (px + vx * 100) % WIDTH
    fy = (py + vy * 100) % HEIGHT

    if fx == mid_x or fy == mid_y:
        continue  # on the dividing line, ignore

    # determine which quadrant
    left  = fx < mid_x
    top   = fy < mid_y
    if top and left:     quadrants[0] += 1
    elif top:            quadrants[1] += 1
    elif left:           quadrants[2] += 1
    else:                quadrants[3] += 1

print(prod(quadrants))
