# Advent of Code 2024 - Day 12: Garden Groups
# Part 2 - Total fencing cost using number of sides instead of perimeter
#
# QUESTION:
# Same regions as Part 1.
# Now cost = area * number_of_sides (instead of area * perimeter).
# A "side" is a straight continuous fence segment — adjacent fence edges
# on the same side of the region that go in the same direction count as ONE side.
#
# APPROACH:
# The number of sides equals the number of corners a region has.
# A cell (r, c) contributes a corner at each of its 4 diagonal positions when:
#   - Convex corner: two adjacent perimeter edges meet (neither neighbor in region)
#   - Concave corner: two adjacent neighbors are in region but the diagonal isn't

import sys
from collections import deque

grid = sys.stdin.read().splitlines()
ROWS, COLS = len(grid), len(grid[0])
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
visited = [[False]*COLS for _ in range(ROWS)]

def count_corners(region_set):
    # corners = sides for any polygon
    corners = 0
    for r, c in region_set:
        # check all 4 diagonal corners of this cell
        for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            # the two orthogonal neighbors at this corner
            side1 = (r+dr, c) in region_set
            side2 = (r, c+dc) in region_set
            diag  = (r+dr, c+dc) in region_set
            # convex corner: both sides are outside the region
            if not side1 and not side2:
                corners += 1
            # concave corner: both sides are in region but diagonal is outside
            elif side1 and side2 and not diag:
                corners += 1
    return corners

total = 0

for sr in range(ROWS):
    for sc in range(COLS):
        if visited[sr][sc]:
            continue
        ch = grid[sr][sc]
        region = []
        q = deque([(sr, sc)])
        visited[sr][sc] = True
        while q:
            r, c = q.popleft()
            region.append((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and not visited[nr][nc] and grid[nr][nc] == ch:
                    visited[nr][nc] = True
                    q.append((nr, nc))

        area = len(region)
        sides = count_corners(set(region))
        total += area * sides

print(total)
