# Advent of Code 2024 - Day 3: Mull It Over
# Part 1 - Extract and Execute mul() Instructions
#
# QUESTION:
# The computer's memory is corrupted. You need to scan through the
# corrupted memory (a string of random characters) and find all valid
# mul(X,Y) instructions, then multiply the numbers and sum the results.
#
# A valid mul instruction looks exactly like: mul(X,Y)
# where X and Y are 1-3 digit numbers. No spaces, no extra characters.
# Invalid ones like mul( 3,7), mul!2,4], or mul(6,9! should be ignored.
#
# Example:
#   xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
#   Valid:  mul(2,4)=8, mul(5,5)=25, mul(11,8)=88, mul(8,5)=40
#   Total: 8 + 25 + 88 + 40 = 161
#
# APPROACH:
# Use regex to find all valid mul(x,y) patterns across the whole input string.
# Treating the entire input as one string is important — instructions can
# span multiple lines.

import re

# read the entire input as one big string (instructions can span lines)
text = "".join(open(0))

# find all valid mul(x,y) patterns and capture both numbers
matches = re.findall(r"mul\((\d+),(\d+)\)", text)

total = 0
for a, b in matches:
    total += int(a) * int(b)

print(total)


# --- rookie approach (keeping it here for reference) ---
# this one breaks input into words first which is messier but also works

# inputs = [list(map(str, line.split())) for line in open(0)]
# all_mul = []
# for i in range(len(inputs)):
#     for j in range(len(inputs[i])):
#         nums = re.findall(r"mul\(\d+,\d+\)", inputs[i][j])
#         abc = re.findall(r"\d+", str(nums))
#         all_mul.append(abc)
# total = 0
# for x in range(len(all_mul)):
#     for y in range(0, len(all_mul[x]), 2):
#         total += (int(all_mul[x][y]) * int(all_mul[x][y+1]))
# print(total)
