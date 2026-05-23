# Advent of Code 2024 - Day 19: Linen Layout
# Part 1 - How many designs are possible?
#
# QUESTION:
# You have a list of towel patterns (e.g. "r", "wr", "bwu", "rb", "gb", "b").
# You need to display specific designs using these patterns concatenated together.
# A pattern can be reused as many times as needed.
# How many of the desired designs can be made?
#
# APPROACH:
# Dynamic programming. dp[i] = True if the first i characters of the design
# can be formed using available patterns.
# For each position, check if any pattern ends here and dp[start] is True.

import sys

data = sys.stdin.read().split('\n\n')
patterns = [p.strip() for p in data[0].split(',')]
designs = data[1].splitlines()

def can_make(design):
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True  # empty string is always achievable
    for i in range(1, n + 1):
        for p in patterns:
            start = i - len(p)
            if start >= 0 and dp[start] and design[start:i] == p:
                dp[i] = True
                break
    return dp[n]

print(sum(1 for d in designs if can_make(d)))
