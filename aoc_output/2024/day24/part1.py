# Advent of Code 2024 - Day 24: Crossed Wires
# Part 1 - Simulate logic gates and get the decimal value of z-wires
#
# QUESTION:
# Input has two sections:
#   Section 1: Initial wire values (e.g. "x00: 1")
#   Section 2: Gate definitions (e.g. "x00 AND y00 -> z00")
# Gates are AND, OR, XOR. Simulate them all and read the z-wires
# (z00, z01, z02, ...) as a binary number (z00 = bit 0). Return its decimal value.
#
# APPROACH:
# Process gates in topological order — keep looping until all wires have values.
# A gate can only fire when both inputs are known.

import sys

data = sys.stdin.read().split('\n\n')
wires = {}
for line in data[0].splitlines():
    name, val = line.split(': ')
    wires[name] = int(val)

gates = []
for line in data[1].splitlines():
    parts = line.split()
    a, op, b, _, out = parts
    gates.append((a, op, b, out))

# keep processing until all outputs are resolved
remaining = list(gates)
while remaining:
    still_pending = []
    for a, op, b, out in remaining:
        if a in wires and b in wires:
            if op == 'AND':   wires[out] = wires[a] & wires[b]
            elif op == 'OR':  wires[out] = wires[a] | wires[b]
            elif op == 'XOR': wires[out] = wires[a] ^ wires[b]
        else:
            still_pending.append((a, op, b, out))
    remaining = still_pending

# read z-wires as a binary number, z00 is the least significant bit
z_wires = sorted((k for k in wires if k.startswith('z')), reverse=True)
binary = ''.join(str(wires[z]) for z in z_wires)
print(int(binary, 2))
