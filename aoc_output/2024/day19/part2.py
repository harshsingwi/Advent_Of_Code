# Advent of Code 2024 - Day 19: Linen Layout
# Part 2 - Count total number of ways to make each design
#
# QUESTION:
# Same patterns and designs as Part 1.
# For each design that IS possible, count how many different ways it can be made.
# Return the sum of all these counts.
#
# APPROACH:
# Same DP, but now dp[i] = number of ways to form the first i characters.
# Instead of stopping at the first match, accumulate all valid paths.

import sys

data = sys.stdin.read().split('\n\n')
patterns = [p.strip() for p in data[0].split(',')]
designs = data[1].splitlines()

def count_ways(design):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1  # one way to make an empty string
    for i in range(1, n + 1):
        for p in patterns:
            start = i - len(p)
            if start >= 0 and dp[start] > 0 and design[start:i] == p:
                dp[i] += dp[start]  # add all ways that got us to `start`
    return dp[n]

print(sum(count_ways(d) for d in designs))
