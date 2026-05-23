# Advent of Code 2024 - Day 17: Chronospatial Computer
# Part 1 - Run the 3-bit computer and get its output
#
# QUESTION:
# A tiny computer with 3 registers (A, B, C) and a program (list of 3-bit numbers).
# Instructions (opcode + operand pairs):
#   0 adv: A = A >> combo(operand)
#   1 bxl: B = B XOR operand
#   2 bst: B = combo(operand) % 8
#   3 jnz: if A != 0, jump to operand
#   4 bxc: B = B XOR C
#   5 out: print combo(operand) % 8
#   6 bdv: B = A >> combo(operand)
#   7 cdv: C = A >> combo(operand)
# Combo operands: 0-3 = literal, 4=A, 5=B, 6=C
# Run the program and return all output values joined by commas.
#
# APPROACH:
# Straight simulation of the instruction set.

import sys
import re

data = sys.stdin.read()
nums = list(map(int, re.findall(r'\d+', data)))
A, B, C = nums[0], nums[1], nums[2]
program = nums[3:]

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
        if A != 0:
            ip = arg
            continue
    elif op == 4: B = B ^ C
    elif op == 5: output.append(combo(arg) % 8)
    elif op == 6: B = A >> combo(arg)
    elif op == 7: C = A >> combo(arg)
    ip += 2

print(','.join(map(str, output)))
