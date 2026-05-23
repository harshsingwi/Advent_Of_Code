# Advent of Code 2024 - Day 3: Mull It Over
# Part 2 - Handle do() and don't() Instructions
#
# QUESTION:
# Same corrupted memory as Part 1, but now there are two more instructions:
#   do()     → enables future mul() instructions
#   don't()  → disables future mul() instructions
#
# At the start, mul() is enabled by default.
# Only count mul(X,Y) results when they appear after a do() (or at the start).
# Ignore any mul() that comes after a don't().
#
# Example:
#   xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
#   mul(2,4) → enabled → +8
#   mul(5,5) → disabled (after don't()) → skip
#   mul(11,8) → still disabled → skip
#   mul(8,5) → re-enabled (after do()) → +40
#   Total: 48
#
# APPROACH:
# Use a single regex that matches all three token types in order: 
# mul(x,y), do(), don't()
# Walk through the matches in order, toggling an "enabled" flag as we go.

import re

text = "".join(open(0))

# match mul(), do(), and don't() tokens — in order of appearance
pattern = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")

enabled = True  # mul() starts enabled
total = 0

for match in pattern.finditer(text):
    token = match.group()

    if token == "do()":
        enabled = True
    elif token == "don't()":
        enabled = False
    else:
        # it's a mul(x,y) — only count it if we're in enabled state
        if enabled:
            a, b = match.groups()
            total += int(a) * int(b)

print(total)
