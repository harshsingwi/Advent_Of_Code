# Advent of Code 2025 - Day 3
# Maximize Sum by Keeping Largest Digit Subsequence
#
# QUESTION:
# Each line is a large number. You must delete digits to produce the largest
# possible number with a fixed number of digits, then sum all results.
#
# Part 1: Keep the largest 6-digit number from each input.
# Part 2: Keep the largest 12-digit number from each input.
#
# The trick: you can't just take the top N digits — ORDER matters.
# e.g. from 12934, keeping 3 digits: best is 934 not 943.
#
# APPROACH:
# Classic "largest number after k deletions" — monotonic stack.
# Pop smaller digits from the stack whenever a larger digit comes along
# and we still have deletions left.

a = []
while True:
    b = input()
    if not b:
        break
    a.append(b)

def find_max(val, keep):
    remove = len(val) - keep  # how many digits to delete
    c = []
    val = str(val)
    for d in val:
        # pop smaller digits while we still can remove more
        while remove > 0 and c and c[-1] < d:
            c.pop()
            remove -= 1
        c.append(d)
    if remove > 0:
        c = c[:-remove]  # if removals left, chop from the end (smallest remain)
    return "".join(c[:keep])

# Part 1: keep largest 6 digits from each number
# count = 0
# for i in range(len(a)):
#     count += int(find_max(a[i], 6))
# print(count)

# Part 2: keep largest 12 digits from each number
count = 0
for i in range(len(a)):
    count += int(find_max(a[i], 12))
print(count)
