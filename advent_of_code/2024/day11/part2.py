# Advent of Code 2024 - Day 11: Plutonian Pebbles
# Part 2 - How many stones after 75 blinks?
#
# QUESTION:
# Exact same rules as Part 1, just 75 blinks instead of 25.
# The number of stones grows exponentially — you absolutely cannot store them all.
# You need the count-based approach from Part 1 to scale.
#
# APPROACH:
# Same dict-of-counts approach — just change 25 to 75.
# The key insight: you only care about HOW MANY stones have each value,
# not which order they're in. The rules are value-based, not position-based.

import sys
from collections import defaultdict

stones = list(map(int, sys.stdin.read().split()))
counts = defaultdict(int)
for s in stones:
    counts[s] += 1

for _ in range(75):
    new_counts = defaultdict(int)
    for val, cnt in counts.items():
        s = str(val)
        if val == 0:
            new_counts[1] += cnt
        elif len(s) % 2 == 0:
            mid = len(s) // 2
            new_counts[int(s[:mid])] += cnt
            new_counts[int(s[mid:])] += cnt
        else:
            new_counts[val * 2024] += cnt
    counts = new_counts

print(sum(counts.values()))
