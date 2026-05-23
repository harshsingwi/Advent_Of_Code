# Advent of Code 2024 - Day 24: Crossed Wires
# Part 2 - Find the 4 swapped output wire pairs in a broken adder circuit
#
# QUESTION:
# The circuit is supposed to compute z = x + y (binary addition).
# But exactly 4 pairs of output wires have been swapped.
# Find the 8 wire names involved in these swaps.
# Output them sorted alphabetically, joined by commas.
#
# APPROACH:
# A ripple-carry adder has a known structure. For each bit position:
#   - Sum bit: XOR of (x_i XOR y_i) with carry_in
#   - Carry out: OR of (x_i AND y_i) with ((x_i XOR y_i) AND carry_in)
# Check each gate against the expected structure and flag anomalies.
# Swapped gates violate the expected pattern.

import sys

data = sys.stdin.read().split('\n\n')
gates = {}
for line in data[1].splitlines():
    parts = line.split()
    a, op, b, _, out = parts
    gates[out] = (a, op, b)

def gate_type(out):
    if out not in gates: return None
    return gates[out][1]

def inputs_of(out):
    if out not in gates: return set()
    a, _, b = gates[out]
    return {a, b}

wrong = set()
max_bit = max(int(k[1:]) for k in gates if k.startswith('z'))

for out, (a, op, b) in gates.items():
    # z-wires (except the last carry) must come from XOR gates
    if out.startswith('z') and op != 'XOR' and out != f'z{max_bit:02d}':
        wrong.add(out)

    # XOR gates should connect to x/y inputs or to z outputs — not to intermediate wires
    if op == 'XOR':
        if not any(w.startswith(('x', 'y', 'z')) for w in [a, b, out]):
            wrong.add(out)

    # AND gates (except x00 AND y00) should feed into OR gates
    if op == 'AND' and 'x00' not in {a, b}:
        for out2, (a2, op2, b2) in gates.items():
            if out in {a2, b2} and op2 != 'OR':
                wrong.add(out)

    # XOR outputs should feed into XOR or AND, not OR
    if op == 'XOR':
        for out2, (a2, op2, b2) in gates.items():
            if out in {a2, b2} and op2 == 'OR':
                wrong.add(out)

print(','.join(sorted(wrong)))
