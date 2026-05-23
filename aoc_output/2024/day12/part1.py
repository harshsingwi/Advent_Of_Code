# Advent of Code 2024 - Day 12: Garden Groups
# Part 1 - Total fencing cost (area * perimeter for each region)
#
# QUESTION:
# The grid contains garden plots marked by letters. Connected cells of the
# same letter form a "region". For each region:
#   - Area = number of cells in the region
#   - Perimeter = number of edges that border either a different region or the grid edge
#   - Cost = area * perimeter
# Return the total cost for all regions.
#
# APPROACH:
# BFS/flood fill to find connected regions. For each region, count cells (area)
# and count edges facing outside the region (perimeter).

import sys
from collections import deque

grid = sys.stdin.read().splitlines()
ROWS, COLS = len(grid), len(grid[0])
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
visited = [[False]*COLS for _ in range(ROWS)]

total = 0

for sr in range(ROWS):
    for sc in range(COLS):
        if visited[sr][sc]:
            continue
        # BFS to find the whole region
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
        region_set = set(region)
        perimeter = 0
        for r, c in region:
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # each edge facing outside the region adds 1 to perimeter
                if (nr, nc) not in region_set:
                    perimeter += 1

        total += area * perimeter

print(total)
