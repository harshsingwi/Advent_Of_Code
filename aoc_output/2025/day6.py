# Advent of Code 2025 - Day 6
# Column-Based Arithmetic Expression Evaluator
#
# QUESTION:
# The input is a grid where expressions are encoded column-by-column.
# Blank columns (all spaces) separate expression groups.
#
# Part 1: Each line is space-separated tokens. When transposed (columns = tokens),
#         each column is [num1, num2, ..., operator]. Eval "op".join(nums).
#
# Part 2: The grid is tightly packed (no spaces between tokens).
#         Each column's last character is the operator.
#         The rest of the characters across each column form the operands.
#         Groups are separated by blank columns.

# --- Part 1 ---
# lines = [line.strip().split() for line in open(0)]
# cols = list(zip(*lines))
# total = 0
# for *nums, op in cols:
#     total += eval(op.join(nums))
# print(total)

# --- Part 2 ---

grid = [line.strip('\n') for line in open(0)]
cols = list(zip(*grid))  # transpose: each col is a vertical slice of the grid

groups = []
group = []

for col in cols:
    if set(col) == {" "}:
        # blank column = separator between expression groups
        groups.append(group)
        group = []
    else:
        group.append(col)

groups.append(group)  # don't lose the last group

count = 0

for group in groups:
    # last char of each column is the operator for this group
    op = group[0][-1]
    # everything except the last char across columns gives us the operand string
    operands = ''.join(''.join(line[:-1]) for line in group)
    count += eval(op.join(operands))

print(count)
