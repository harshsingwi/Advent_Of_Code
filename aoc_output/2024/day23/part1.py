# Advent of Code 2024 - Day 23: LAN Party
# Part 1 - Count triangles containing at least one 't' computer
#
# QUESTION:
# Input is a list of connections between computers (e.g. "kh-tc").
# Find all sets of THREE mutually connected computers (triangles in the graph).
# Count those where at least one computer name starts with 't'.
#
# APPROACH:
# Build adjacency sets. For each edge (a,b), check all common neighbors c
# where (a,c) and (b,c) also exist — that's a triangle.
# Use frozenset to avoid counting the same triangle multiple times.

import sys
from collections import defaultdict

lines = sys.stdin.read().splitlines()
adj = defaultdict(set)
for line in lines:
    a, b = line.split('-')
    adj[a].add(b)
    adj[b].add(a)

triangles = set()
for a in adj:
    for b in adj[a]:
        for c in adj[a] & adj[b]:  # c is connected to both a and b
            triangles.add(frozenset([a, b, c]))

# count triangles where at least one node starts with 't'
count = sum(1 for t in triangles if any(n.startswith('t') for n in t))
print(count)
