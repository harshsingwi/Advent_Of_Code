# Advent of Code 2024 - Day 18: RAM Run
# Part 2 - Find the first byte that cuts off the exit
#
# QUESTION:
# Same setup. Find the FIRST byte that, when it falls, makes it impossible
# to reach (70,70) from (0,0). Output its coordinates as "x,y".
#
# APPROACH:
# Binary search over the number of bytes fallen.
# If path exists with k bytes → try more. If path blocked → try fewer.
# BFS for reachability check.

import sys
from collections import deque

coords = [tuple(map(int, line.split(','))) for line in sys.stdin.read().splitlines()]
SIZE = 70
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def can_reach(n):
    blocked = set(coords[:n])
    q = deque([(0, 0)])
    visited = {(0, 0)}
    while q:
        r, c = q.popleft()
        if r == SIZE and c == SIZE:
            return True
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr <= SIZE and 0 <= nc <= SIZE and (nr, nc) not in visited and (nc, nr) not in blocked:
                visited.add((nr, nc))
                q.append((nr, nc))
    return False

lo, hi = 1024, len(coords)
while lo < hi:
    mid = (lo + hi) // 2
    if can_reach(mid):
        lo = mid + 1
    else:
        hi = mid

# coords[lo-1] is the first byte that blocks the path
x, y = coords[lo - 1]
print(f"{x},{y}")
