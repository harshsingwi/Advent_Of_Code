# Advent of Code 2024 - Day 11: Plutonian Pebbles
# Part 1 - How many stones after 25 blinks?
#
# QUESTION:
# You have a row of stones, each engraved with a number.
# Every "blink", ALL stones transform simultaneously:
#   - If the stone is 0 → becomes 1
#   - If the stone has an even number of digits → splits into two stones
#     (left half of digits, right half of digits — no leading zeros)
#   - Otherwise → stone's number is multiplied by 2024
#
# How many stones are there after 25 blinks?
#
# Example: 0 1 10 99 999
#   After 1 blink: 1 2024 1 0 9 9 2021976
#
# APPROACH:
# Track stone counts in a dictionary (value → count), not a list.
# Many stones will have the same number, so we count them together.
# Each blink, build a new dict applying the rules to each unique value.

import sys
from collections import defaultdict

stones = list(map(int, sys.stdin.read().split()))
counts = defaultdict(int)
for s in stones:
    counts[s] += 1

for _ in range(25):
    new_counts = defaultdict(int)
    for val, cnt in counts.items():
        s = str(val)
        if val == 0:
            new_counts[1] += cnt
        elif len(s) % 2 == 0:
            # split into two halves
            mid = len(s) // 2
            new_counts[int(s[:mid])] += cnt
            new_counts[int(s[mid:])] += cnt
        else:
            new_counts[val * 2024] += cnt
    counts = new_counts

print(sum(counts.values()))
