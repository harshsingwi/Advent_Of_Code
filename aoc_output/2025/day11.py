# Advent of Code 2025 - Day 11
# Count Paths Through a DAG That Pass Through Two Specific Nodes
#
# QUESTION:
# Same structure as Day 9 — directed acyclic graph with a sink node 'out'.
# Input format:
#   node_name: child1 child2 child3 ...
#
# Part 1: Count ALL paths from 'svr' to 'out'.
# Part 2: Count paths from 'svr' to 'out' that pass through BOTH 'fft' AND 'dac'.
#
# This is the same problem as Day 9 but with a different (likely larger/harder) graph.
#
# APPROACH:
# Memoized DFS with lru_cache.
# State = (node, seen_fft, seen_dac) — the two booleans let us track which
# required nodes have been visited without losing the ability to cache.

graph = dict(
    (k, v.split())
    for k, v in
    (line.strip().split(':') for line in open(0))
)

from functools import lru_cache

# --- Part 1: count all paths ---
# def counter(graph, val):
#     if graph[val] == ['out']:
#         return 1
#     total = 0
#     for nxt in graph[val]:
#         total += counter(graph, nxt)
#     return total
# print(counter(graph, 'svr'))

# --- Part 2: paths that visit both 'fft' and 'dac' ---
def count_paths_with_both(graph, start, a, b):
    @lru_cache(None)
    def dfs(node, seen_a, seen_b):
        if node == 'out':
            return 1 if seen_a and seen_b else 0

        total = 0
        for nxt in graph[node]:
            total += dfs(
                nxt,
                seen_a or (nxt == a),  # flip to True the moment we hit node a
                seen_b or (nxt == b)   # same for node b
            )
        return total

    return dfs(start, start == a, start == b)

count = count_paths_with_both(graph, 'svr', 'fft', 'dac')
print(count)
