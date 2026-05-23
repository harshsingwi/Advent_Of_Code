# Advent of Code 2024 - Day 1: Historian Hysteria
# Part 2 - Similarity Score
#
# QUESTION:
# Same input as Part 1 - two lists of location IDs.
# This time, calculate a "similarity score" instead of distance.
#
# For each number in the left list, count how many times it appears
# in the right list. Multiply the number by its count, and add it to
# the running total.
#
# Example:
#   Left:  3, 4, 2, 1, 3, 3
#   Right: 4, 3, 5, 3, 9, 3
#   3 appears 3 times in right → 3*3 = 9, and 3 appears 3 times in left → 9+9+9
#   4 appears 1 time in right  → 4*1 = 4
#   2 appears 0 times in right → 2*0 = 0
#   ...and so on
#
# APPROACH:
# Build a frequency table (dict) for the right list,
# then for each number in the left list, multiply it by its count in the dict.
# Using a dict makes lookups O(1) instead of O(n).

left = []
right = []

while True:
    try:
        a, b = map(int, input().split())
        left.append(a)
        right.append(b)
    except EOFError:
        break

# count how many times each number appears in the right list
table = {}
for i in range(len(right)):
    if right[i] in table:
        table[right[i]] += 1
    else:
        table[right[i]] = 1

total = 0
for j in range(len(left)):
    try:
        # multiply left number by how many times it shows up in right
        total += (left[j] * table[left[j]])
    except KeyError:
        # number doesn't appear in right list at all, skip it (contributes 0)
        continue

print(total)
