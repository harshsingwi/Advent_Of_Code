# Advent of Code 2025 - Day 8
# Maximum Area Rectangle from Coordinate Pairs
#
# QUESTION:
# Input: a list of 2D points as "x,y" (one per line).
# Each pair of points can form an axis-aligned rectangle as opposite corners.
# Area = (|x1 - x2| + 1) * (|y1 - y2| + 1)
#
# Part 1: For each point, find the point farthest from it (max Manhattan distance)
#         and return the sum of all those max distances.
# Part 2: Find the single pair of points that forms the LARGEST rectangle area.
#
# APPROACH (Part 2):
# Brute force O(n^2) over all unique pairs.
# Using enumerate + grid[:i] avoids counting the same pair twice.

grid = [list(map(int, line.split(','))) for line in open(0)]

# --- Part 1: for each point, find max Manhattan distance to any other point ---
# total = 0
# for i, (x1, y1) in enumerate(grid):
#     max_dist = max(abs(x1 - x2) + abs(y1 - y2) for x2, y2 in grid if (x2, y2) != (x1, y1))
#     total += max_dist
# print(total)

# --- Part 2: find the pair that forms the largest bounding rectangle ---
print(max(
    (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    for i, (x1, y1) in enumerate(grid)
    for x2, y2 in grid[:i]  # only look at earlier points to avoid duplicate pairs
))
