# Advent of Code 2024 - Day 5: Print Queue
# Part 1 - Find correctly ordered updates and sum their middle pages
#
# QUESTION:
# The elves need to print safety manuals. You're given:
#   Section 1: Page ordering rules like "X|Y" meaning X must come before Y
#   Section 2: Updates — each is a comma-separated list of page numbers
#
# An update is "correctly ordered" if for every rule X|Y, whenever both X and Y
# appear in the update, X comes before Y.
#
# Find all correctly ordered updates, and for each one take the middle page number.
# Return the sum of all those middle pages.
#
# Example:
#   Rules: 47|53, 97|13, 97|61, ...
#   Update: 75,47,61,53,29 → correctly ordered → middle = 61
#   Update: 61,13,29 → correctly ordered → middle = 13
#   Update: 75,97,47,61,53 → WRONG order (97 should come before 75) → skip
#
# APPROACH:
# Build a set of (before, after) pairs from the rules.
# For each update, check every pair of pages — if (later_page, earlier_page) is
# in the rules set, the order is wrong. If all pairs are fine, grab the middle element.

import sys
from collections import defaultdict

data = sys.stdin.read().strip().split('\n\n')
rules_raw = data[0].splitlines()
updates_raw = data[1].splitlines()

# store rules as a set of (X, Y) meaning X must come before Y
rules = set()
for line in rules_raw:
    a, b = line.split('|')
    rules.add((a.strip(), b.strip()))

def is_correct(update):
    # check every pair: if the later page should come before the earlier one, it's wrong
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if (update[j], update[i]) in rules:
                return False
    return True

total = 0
for line in updates_raw:
    update = line.split(',')
    if is_correct(update):
        mid = update[len(update) // 2]
        total += int(mid)

print(total)
