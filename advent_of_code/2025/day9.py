# Advent of Code 2025 - Day 9
# Count Paths Through a DAG
#
# QUESTION:
# Directed acyclic graph where each node maps to its children.
# Special sink node is 'out'. Input format:
#   node_name: child1 child2 child3 ...
#
# Part 1: Count ALL paths from 'svr' to 'out'.
# Part 2: Count paths from 'svr' to 'out' that pass through BOTH 'fft' AND 'dac'.
#
# APPROACH:
# Memoized DFS. For Part 2, the state includes two boolean flags tracking
# whether we've visited each of the two required nodes.
# lru_cache makes repeated subpath lookups O(1).

graph = dict(
    (k, v.split())
    for k, v in
    (line.strip().split(':') for line in open(0))
)

from functools import lru_cache

# --- Part 1: count all paths from svr to out ---
# def counter(graph, val):
#     if graph[val] == ['out']:
#         return 1
#     total = 0
#     for nxt in graph[val]:
#         total += counter(graph, nxt)
#     return total
# print(counter(graph, 'svr'))

# --- Part 2: count paths that visit both 'fft' and 'dac' ---
def count_paths_with_both(graph, start, a, b):
    @lru_cache(None)
    def dfs(node, seen_a, seen_b):
        if node == 'out':
            return 1 if seen_a and seen_b else 0  # only valid if both were visited

        total = 0
        for nxt in graph[node]:
            total += dfs(
                nxt,
                seen_a or (nxt == a),  # flip flag the moment we step on target a
                seen_b or (nxt == b)   # same for b
            )
        return total

    return dfs(start, start == a, start == b)

count = count_paths_with_both(graph, 'svr', 'fft', 'dac')
print(count)
