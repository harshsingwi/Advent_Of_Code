# Advent of Code 2024 - Day 7: Bridge Repair
# Part 1 - Which equations can be made true using + and * ?
#
# QUESTION:
# Each line has a target value followed by a list of numbers.
# Insert + or * between the numbers (left to right, no precedence rules)
# to see if you can produce the target value.
# Sum up the target values of all equations that CAN be made true.
#
# Example:
#   190: 10 19       → 10 * 19 = 190 ✓
#   3267: 81 40 27   → 81 * 40 + 27 = 3267 OR 81 + 40 * 27 ✓
#   83: 17 5         → 17 + 5 = 22, 17 * 5 = 85 — neither is 83 ✗
#
# APPROACH:
# Recursive DFS — at each step try adding or multiplying the next number
# to the running total. If we reach the end and match the target, it's valid.
# Pruning: stop early if running total already exceeds target (since all nums > 0).

import sys

lines = sys.stdin.read().splitlines()

def can_make(target, nums, i, current):
    if i == len(nums):
        return current == target
    if current > target:
        return False  # early exit — can only grow from here
    return (can_make(target, nums, i + 1, current + nums[i]) or
            can_make(target, nums, i + 1, current * nums[i]))

total = 0
for line in lines:
    left, right = line.split(': ')
    target = int(left)
    nums = list(map(int, right.split()))
    if can_make(target, nums, 1, nums[0]):
        total += target

print(total)
