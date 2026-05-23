# Advent of Code 2024 - Day 5: Print Queue
# Part 2 - Fix incorrectly ordered updates and sum their middle pages
#
# QUESTION:
# Same input as Part 1.
# This time, find all the INCORRECTLY ordered updates.
# Sort each one using the ordering rules, then take the middle page.
# Return the sum of the middle pages of all the fixed updates.
#
# APPROACH:
# Reuse the is_correct() check to find bad updates.
# Sort each bad update using a custom comparator:
#   if (a, b) is in rules → a goes before b (return -1)
#   if (b, a) is in rules → b goes before a (return +1)
#   otherwise → equal, don't care
# Python's functools.cmp_to_key lets us use a comparator function with sorted().

import sys
from functools import cmp_to_key

data = sys.stdin.read().strip().split('\n\n')
rules_raw = data[0].splitlines()
updates_raw = data[1].splitlines()

rules = set()
for line in rules_raw:
    a, b = line.split('|')
    rules.add((a.strip(), b.strip()))

def is_correct(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if (update[j], update[i]) in rules:
                return False
    return True

def compare(a, b):
    # if a must come before b, a is "smaller" in sort order
    if (a, b) in rules:
        return -1
    if (b, a) in rules:
        return 1
    return 0

total = 0
for line in updates_raw:
    update = line.split(',')
    if not is_correct(update):
        # fix the order using the rules as a comparator
        fixed = sorted(update, key=cmp_to_key(compare))
        mid = fixed[len(fixed) // 2]
        total += int(mid)

print(total)
