# Advent of Code 2024 - Day 7: Bridge Repair
# Part 2 - Same but now also allow || (concatenation) as an operator
#
# QUESTION:
# Same as Part 1, but now there's a third operator: ||
# The || operator concatenates the digits of two numbers.
# Example: 12 || 345 = 12345
#
# Find all equations that can be made true with +, *, or ||
# and sum their target values.
#
# APPROACH:
# Same recursive DFS as Part 1, just add a third branch for concatenation.
# Concatenation: int(str(a) + str(b)) — simple and readable.

import sys

lines = sys.stdin.read().splitlines()

def can_make(target, nums, i, current):
    if i == len(nums):
        return current == target
    if current > target:
        return False
    # try all three operators: add, multiply, concatenate
    return (can_make(target, nums, i + 1, current + nums[i]) or
            can_make(target, nums, i + 1, current * nums[i]) or
            can_make(target, nums, i + 1, int(str(current) + str(nums[i]))))

total = 0
for line in lines:
    left, right = line.split(': ')
    target = int(left)
    nums = list(map(int, right.split()))
    if can_make(target, nums, 1, nums[0]):
        total += target

print(total)
