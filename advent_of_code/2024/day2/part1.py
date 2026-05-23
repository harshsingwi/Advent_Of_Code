# Advent of Code 2024 - Day 2: Red-Nosed Reports
# Part 1 - Count Safe Reports
#
# QUESTION:
# The engineers at the Red-Nosed reactor give you a list of reports.
# Each report is a list of numbers called "levels".
# A report is SAFE if both of these are true:
#   1. The levels are either ALL increasing or ALL decreasing.
#   2. Any two adjacent levels differ by at least 1 and at most 3.
#
# How many reports are safe?
#
# Example:
#   7 6 4 2 1 → Safe (all decreasing, diffs are 1,2,1,1)
#   1 2 7 8 9 → Unsafe (2→7 is a jump of 5, too big)
#   9 7 6 2 1 → Unsafe (6→2 is a jump of 4, too big)
#   1 3 2 4 5 → Unsafe (1→3 is up but 3→2 is down, direction changes)
#   8 6 4 4 1 → Unsafe (4→4 has no change, needs at least 1)
#   1 3 6 7 9 → Safe (all increasing, diffs are 2,3,1,2)
#
# APPROACH:
# Check the first pair to determine direction (ascending or descending),
# then verify every adjacent pair follows the same direction with a diff of 1-3.

inputs = [list(map(int, line.split())) for line in open(0)]

def is_safe(arr):
    # check if the sequence is increasing with valid step sizes
    if arr[0] < arr[1] and 0 < abs(arr[0] - arr[1]) <= 3:
        for i in range(1, len(arr) - 1):
            if arr[i] < arr[i + 1] and 0 < abs(arr[i] - arr[i + 1]) <= 3:
                pass
            else:
                return False
        return True

    # check if the sequence is decreasing with valid step sizes
    elif arr[0] > arr[1] and 0 < abs(arr[0] - arr[1]) <= 3:
        for j in range(1, len(arr) - 1):
            if arr[j] > arr[j + 1] and 0 < abs(arr[j] - arr[j + 1]) <= 3:
                pass
            else:
                return False
        return True

    else:
        # first two elements are equal or differ by more than 3, already unsafe
        return False

count = 0
for i in range(len(inputs)):
    if is_safe(inputs[i]):
        count += 1

print(count)
