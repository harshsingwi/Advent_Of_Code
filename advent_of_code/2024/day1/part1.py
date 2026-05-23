# Advent of Code 2024 - Day 1: Historian Hysteria
# Part 1 - Total Distance Between Lists
#
# QUESTION:
# The Chief Historian is missing! The Senior Historians need your help.
# You're given two lists of location IDs (one per column in the input).
# Your job is to figure out how "different" the two lists are.
#
# Pair up the numbers by sorting both lists, then match the smallest with
# the smallest, second smallest with second smallest, and so on.
# Calculate the absolute difference for each pair, and return the total sum.
#
# Example:
#   Left:  3, 4, 2, 1, 3, 3
#   Right: 4, 3, 5, 3, 9, 3
#   Sorted pairs: (1,3), (2,3), (3,3), (3,4), (3,5), (4,9)
#   Differences:    2  +  1  +  0  +  1  +  2  +  5  = 11
#
# APPROACH:
# Read both columns into separate lists, sort them both,
# then walk through them together and sum the absolute differences.

left = []
right = []

while True:
    try:
        a, b = map(int, input().split())
        left.append(a)
        right.append(b)
    except EOFError:
        break

# sort both lists so we can pair smallest with smallest
left.sort()
right.sort()

total = 0
for i in range(len(left)):
    total += abs(left[i] - right[i])

print(total)
