# Advent of Code 2024 - Day 21: Keypad Conundrum
# Part 2 - Same but now 25 directional robots in the chain
#
# QUESTION:
# Same as Part 1, but now there are 25 directional robot keypads between you
# and the numeric keypad (instead of 2). Find minimum presses and complexities.
#
# APPROACH:
# Exactly the same code as Part 1 — just change depth from 2 to 25.
# The memoization handles the exponential growth elegantly.

import sys
from collections import deque
from functools import lru_cache

num_pad = {
    '7':(0,0),'8':(0,1),'9':(0,2),
    '4':(1,0),'5':(1,1),'6':(1,2),
    '1':(2,0),'2':(2,1),'3':(2,2),
              '0':(3,1),'A':(3,2)
}
dir_pad = {
              '^':(0,1),'A':(0,2),
    '<':(1,0),'v':(1,1),'>':(1,2)
}
move_dirs = {'^':(-1,0),'v':(1,0),'<':(0,-1),'>':(0,1)}

def bfs_paths(pad):
    positions = {v: k for k, v in pad.items()}
    paths = {}
    for start in pad:
        for end in pad:
            if start == end:
                paths[(start, end)] = ['A']
                continue
            sr, sc = pad[start]
            q = deque([(sr, sc, '')])
            visited = {(sr, sc)}
            found = []
            best = float('inf')
            while q:
                r, c, path = q.popleft()
                if len(path) > best: break
                if (r, c) == pad[end]:
                    found.append(path + 'A')
                    best = len(path)
                    continue
                for d, (dr, dc) in move_dirs.items():
                    nr, nc = r+dr, c+dc
                    if (nr, nc) in positions and (nr, nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr, nc, path+d))
            paths[(start, end)] = found
    return paths

num_paths = bfs_paths(num_pad)
dir_paths = bfs_paths(dir_pad)

@lru_cache(maxsize=None)
def min_presses(seq, depth):
    if depth == 0:
        return len(seq)
    total = 0
    cur = 'A'
    for ch in seq:
        options = dir_paths[(cur, ch)]
        total += min(min_presses(opt, depth - 1) for opt in options)
        cur = ch
    return total

codes = sys.stdin.read().splitlines()
result = 0
for code in codes:
    cur = 'A'
    total = 0
    for ch in code:
        options = num_paths[(cur, ch)]
        total += min(min_presses(opt, 25) for opt in options)  # 25 robots now
        cur = ch
    result += total * int(code[:-1])

print(result)
