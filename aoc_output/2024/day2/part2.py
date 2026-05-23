# Advent of Code 2024 - Day 2: Red-Nosed Reports
# Part 2 - Problem Dampener
#
# QUESTION:
# Same as Part 1, but now the reactor has a "Problem Dampener" module.
# This lets you tolerate a single bad level in an otherwise safe report.
#
# If a report is NOT safe, check if removing any single level from it
# would make it safe. If yes, count it as safe.
#
# Example (same reports as Part 1):
#   7 6 4 2 1 → Safe (was already safe)
#   1 2 7 8 9 → Unsafe (no single removal helps)
#   9 7 6 2 1 → Unsafe (no single removal helps)
#   1 3 2 4 5 → Safe! removing 3 gives [1,2,4,5] which is safe
#   8 6 4 4 1 → Safe! removing one 4 gives [8,6,4,1] which is safe
#   1 3 6 7 9 → Safe (was already safe)
# → 4 safe reports total
#
# APPROACH:
# Reuse the is_safe() check from Part 1.
# For the dampener: try removing each element one by one and check
# if the resulting list passes is_safe(). This is O(n^2) but input is small.

inputs = [list(map(int, line.split())) for line in open(0)]

def is_safe(arr):
    if arr[0] < arr[1] and 0 < abs(arr[0] - arr[1]) <= 3:
        for i in range(1, len(arr) - 1):
            if arr[i] < arr[i + 1] and 0 < abs(arr[i] - arr[i + 1]) <= 3:
                pass
            else:
                return False
        return True

    elif arr[0] > arr[1] and 0 < abs(arr[0] - arr[1]) <= 3:
        for j in range(1, len(arr) - 1):
            if arr[j] > arr[j + 1] and 0 < abs(arr[j] - arr[j + 1]) <= 3:
                pass
            else:
                return False
        return True
    else:
        return False

def is_safe_with_dampener(arr):
    # if it's already safe, no need to do anything
    if is_safe(arr):
        return True

    # try removing each element and see if the remaining list becomes safe
    for i in range(len(arr)):
        new_arr = arr[:i] + arr[i + 1:]
        if is_safe(new_arr):
            return True

    return False

count = 0
for report in inputs:
    if is_safe_with_dampener(report):
        count += 1

print(count)
