# Advent of Code 2025 - Day 2
# Repeating Pattern Numbers
#
# QUESTION:
# Input: comma-separated ranges like "10-99,100-999"
# A number is "invalid" (a repeating pattern number) if its digits can be
# split into equal chunks where every chunk is identical.
#   e.g. 1212 → "12","12" → repeating → invalid
#        1111 → "1","1","1","1" → repeating → invalid
#        1234 → no valid split → valid
#
# Part 1: Count how many invalid numbers exist across all ranges.
# Part 2: Print the invalid numbers and return their sum.

inputs = input()
a = [list(map(int, part.split('-'))) for part in inputs.split(',')]

invalid = []

def if_invalid(value):
    value = str(value)
    length = len(value)
    for i in range(1, length // 2 + 1):
        if chunk_possible(value, i) and compare_all(value, i):
            return True
    return False

def chunk_possible(number, chunk):
    # can only split evenly if length divides by chunk size
    return len(number) % int(chunk) == 0

def compare_all(number, chunk):
    # split into chunks and check they're all identical
    parts = []
    chunk = int(chunk)
    for i in range(0, len(number), chunk):
        parts.append(number[i:i + chunk])
    for j in range(len(parts) - 1):
        if parts[j] != parts[j + 1]:
            return False
    return True

for i in range(len(a)):
    start, end = a[i]
    for j in range(start, end + 1):
        if if_invalid(j):
            invalid.append(j)

# Part 1: just the count
# print(len(invalid))

# Part 2: list them out and sum them
print(invalid)
print(sum(invalid))
