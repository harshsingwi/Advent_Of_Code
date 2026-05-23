# Advent of Code 2024 - Day 22: Monkey Market
# Part 1 - Sum of 2000th secret numbers
#
# QUESTION:
# Each buyer starts with a secret number. Each step evolves the secret:
#   1. result = secret * 64;    secret = (secret XOR result) % 16777216
#   2. result = secret // 32;   secret = (secret XOR result) % 16777216
#   3. result = secret * 2048;  secret = (secret XOR result) % 16777216
# Evolve each secret 2000 times. Sum all the resulting 2000th values.
#
# APPROACH:
# Straight simulation. The modulo is 2^24 = 16777216.

import sys

def evolve(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ (secret // 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret

total = 0
for line in sys.stdin.read().splitlines():
    s = int(line)
    for _ in range(2000):
        s = evolve(s)
    total += s

print(total)
