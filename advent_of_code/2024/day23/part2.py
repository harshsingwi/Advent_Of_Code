# Advent of Code 2024 - Day 23: LAN Party
# Part 2 - Find the largest clique (the LAN party)
#
# QUESTION:
# Same graph as Part 1.
# Find the largest set of computers where every pair is connected.
# This is the maximum clique problem.
# Output the computers in that clique sorted alphabetically, joined by commas.
#
# APPROACH:
# Bron-Kerbosch algorithm with pivoting — the standard max clique algorithm.
# Works well enough for the AoC input size.

import sys
from collections import defaultdict

lines = sys.stdin.read().splitlines()
adj = defaultdict(set)
for line in lines:
    a, b = line.split('-')
    adj[a].add(b)
    adj[b].add(a)

nodes = list(adj.keys())
best = []

def bron_kerbosch(R, P, X):
    global best
    if not P and not X:
        if len(R) > len(best):
            best = list(R)
        return
    # pivot: choose node in P∪X with most neighbors in P (reduces branches)
    pivot = max(P | X, key=lambda v: len(adj[v] & P))
    for v in list(P - adj[pivot]):
        bron_kerbosch(R | {v}, P & adj[v], X & adj[v])
        P.remove(v)
        X.add(v)

bron_kerbosch(set(), set(nodes), set())
print(','.join(sorted(best)))
