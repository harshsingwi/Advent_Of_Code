# Advent of Code 2025 - Day 5
# Range Coverage Problems
#
# QUESTION:
# Input has two sections (blank line separator):
#   Section 1: Ranges as "start-end" (one per line)
#   Section 2: Individual integers (one per line)
#
# Part 1: For each integer in section 2, check if it falls within ANY range.
#         Count how many integers are "covered" by at least one range.
#
# Part 2: Merge all overlapping ranges together, then count the total number
#         of integers covered by the merged ranges.
#
# APPROACH (Part 2):
# Sort ranges by start, then walk through merging overlapping ones.
# Sum the length of each merged range.

a = []
while True:
    line = input().strip()
    if not line:
        break
    a.append(list(map(int, line.split('-'))))

b = []
while True:
    line = input().strip()
    if not line:
        break
    b.append(int(line))

# --- Part 1: count integers from section 2 that fall in any range ---
count = 0
for x in b:
    for start, end in a:
        if start <= x <= end:
            count += 1
            break  # only count each integer once even if multiple ranges cover it
# print(count)

# --- Part 2: merge overlapping ranges, count total integers covered ---
a.sort()  # sort by start of range
new = []
current = a[0]

for i in range(1, len(a)):
    if current[0] <= a[i][0] <= current[1]:
        # this range overlaps current — extend if it reaches further
        current = [current[0], max(current[1], a[i][1])]
    else:
        new.append(current)
        current = a[i]

new.append(current)

count = 0
for i in range(len(new)):
    count += new[i][1] - new[i][0] + 1

print(count)
