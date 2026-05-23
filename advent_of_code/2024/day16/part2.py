# Advent of Code 2024 - Day 16: Reindeer Maze
# Part 2 - Count tiles that are part of ANY best path
#
# QUESTION:
# Same maze as Part 1.
# Find the number of distinct tiles that appear on at least one optimal path
# (a path with the minimum possible score).
#
# APPROACH:
# Run Dijkstra forward from S to get min cost to reach every state.
# Run Dijkstra backward from E (reversing all edges) to get min cost from E.
# A tile (r,c) is on an optimal path if:
#   dist_forward[r,c,d] + dist_backward[r,c,d] == best_score
# for any direction d.

import sys
import heapq

grid = sys.stdin.read().splitlines()
ROWS, COLS = len(grid), len(grid[0])

S = next((r,c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 'S')
E = next((r,c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 'E')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dijkstra(starts):
    dist = {}
    heap = list(starts)
    heapq.heapify(heap)
    while heap:
        cost, r, c, d = heapq.heappop(heap)
        if (r, c, d) in dist:
            continue
        dist[(r, c, d)] = cost
        # forward step
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != '#':
            if (nr, nc, d) not in dist:
                heapq.heappush(heap, (cost + 1, nr, nc, d))
        # turns
        for turn in [-1, 1]:
            nd = (d + turn) % 4
            if (r, c, nd) not in dist:
                heapq.heappush(heap, (cost + 1000, r, c, nd))
    return dist

# forward from S facing East
fwd = dijkstra([(0, S[0], S[1], 0)])

# backward from E in all directions (reverse move = come from in front of us)
# for reverse: moving "backward" means the cost is still 1 for a step, 1000 for a turn
# we start at E in all 4 directions with cost 0 (since we're searching backwards)
bwd = dijkstra([(0, E[0], E[1], d) for d in range(4)])

best_score = min(fwd.get((E[0], E[1], d), float('inf')) for d in range(4))

# collect all tiles on any optimal path
good_tiles = set()
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == '#':
            continue
        for d in range(4):
            f = fwd.get((r, c, d), float('inf'))
            # backward: we arrived from direction d, so in reverse we're facing opposite
            b = bwd.get((r, c, (d + 2) % 4), float('inf'))
            if f + b == best_score:
                good_tiles.add((r, c))

print(len(good_tiles))
