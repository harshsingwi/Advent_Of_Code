# Advent of Code 2024 - Day 17: Chronospatial Computer
# Part 2 - Find initial value of A that makes program output itself (quine)
#
# QUESTION:
# Same computer as Part 1.
# Find the smallest initial value for register A such that the program
# outputs a copy of itself (a quine).
#
# APPROACH:
# The program processes A in chunks of 3 bits at a time (right shift by 3 each loop).
# Work backwards: find A 3 bits at a time from the end of the target output.
# For each partial solution, try all 8 possible next 3-bit chunks (0-7),
# run the program, and keep only those that match the remaining suffix of the target.

import sys
import re

data = sys.stdin.read()
nums = list(map(int, re.findall(r'\d+', data)))
init_B, init_C = nums[1], nums[2]
program = nums[3:]

def run(A):
    B, C = init_B, init_C
    ip = 0
    output = []
    def combo(op):
        if op <= 3: return op
        if op == 4: return A
        if op == 5: return B
        if op == 6: return C
    while ip < len(program):
        op, arg = program[ip], program[ip+1]
        if op == 0: A = A >> combo(arg)
        elif op == 1: B = B ^ arg
        elif op == 2: B = combo(arg) % 8
        elif op == 3:
            if A != 0: ip = arg; continue
        elif op == 4: B = B ^ C
        elif op == 5: output.append(combo(arg) % 8)
        elif op == 6: B = A >> combo(arg)
        elif op == 7: C = A >> combo(arg)
        ip += 2
    return output

# build A backwards, 3 bits at a time
candidates = [0]
for target in reversed(program):
    next_candidates = []
    for base in candidates:
        for bits in range(8):
            A = (base << 3) | bits
            out = run(A)
            if out and out[0] == target:
                next_candidates.append(A)
    candidates = next_candidates

print(min(candidates))
