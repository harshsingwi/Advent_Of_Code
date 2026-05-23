# Advent of Code 2024 - Day 21: Keypad Conundrum
# Part 1 - Shortest button sequence through 2 directional robots + 1 numpad robot
#
# QUESTION:
# You control a directional keypad. That controls robot 1's directional keypad.
# Robot 1 controls robot 2's directional keypad.
# Robot 2 controls a numeric keypad that types the actual codes.
# Find the shortest sequence of YOUR button presses to type each 4-digit code.
# Complexity = len(sequence) * numeric_part_of_code. Sum all complexities.
#
# Numeric keypad layout:      Directional keypad:
#   7 8 9                         . ^ A
#   4 5 6                         < v >
#   1 2 3
#     0 A
#
# APPROACH:
# Use BFS to precompute shortest move sequences between any two keys on each pad.
# Then use memoized recursion to find the minimum total button presses
# for a sequence at a given depth of robot indirection.

import sys
from collections import deque
from functools import lru_cache
from itertools import product

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
    # find all shortest paths between every pair of keys on this pad
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
    # depth=0 means you type it yourself — cost is just the length
    if depth == 0:
        return len(seq)
    total = 0
    cur = 'A'  # all arms start at 'A'
    for ch in seq:
        # find the cheapest way to move from cur to ch at the next level up
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
        total += min(min_presses(opt, 2) for opt in options)  # 2 directional robots
        cur = ch
    result += total * int(code[:-1])

print(result)
