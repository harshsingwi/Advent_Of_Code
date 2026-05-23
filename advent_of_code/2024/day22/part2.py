# Advent of Code 2024 - Day 22: Monkey Market
# Part 2 - Maximum bananas from best 4-change sequence
#
# QUESTION:
# Same secret evolution as Part 1.
# The price at each step = last digit of the secret (secret % 10).
# A monkey sells when it sees a specific sequence of 4 consecutive price CHANGES.
# Each buyer sells at the FIRST occurrence of that sequence.
# Find the 4-change sequence that maximizes the total bananas across all buyers.
#
# APPROACH:
# For each buyer, generate 2000 prices and their changes.
# Slide a window of 4 changes — record the price at first occurrence per buyer.
# Use a dict to accumulate total bananas per sequence across all buyers.

import sys
from collections import defaultdict

def evolve(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret

totals = defaultdict(int)

for line in sys.stdin.read().splitlines():
    s = int(line)
    prices = [s % 10]
    for _ in range(2000):
        s = evolve(s)
        prices.append(s % 10)

    changes = [prices[i+1] - prices[i] for i in range(len(prices)-1)]

    seen = set()
    for i in range(len(changes) - 3):
        seq = (changes[i], changes[i+1], changes[i+2], changes[i+3])
        if seq not in seen:
            seen.add(seq)
            totals[seq] += prices[i+4]  # the price after the 4th change

print(max(totals.values()))
