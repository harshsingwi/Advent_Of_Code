# Advent of Code 2025 - Day 1
# Circular Array Navigation: Count Zero Crossings
#
# QUESTION:
# You have a circular array of 100 elements (indices 0..99).
# Start at index 50. Each instruction is either "R<n>" or "L<n>".
#
# Part 1: Just return your final index after all moves.
# Part 2: Count how many times you cross or land on index 0 during all moves.
#
# Example:
#   R60 from index 50 → new index is 10, crossed index 0 once
#   L5  from index 10 → new index is 5, no zero crossing

class Solution:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)

    def go_right(self, index, steps):
        # modulo handles the wrap-around naturally
        return (index + steps) % self.length

    def go_right_time(self, index, steps):
        # how many times do we cross index 0 going right by `steps` from `index`?
        if steps == 0:
            return 0
        # distance to first hit of index 0 going right
        first_zero_dist = self.length if index == 0 else self.length - index
        if steps < first_zero_dist:
            return 0
        return 1 + (steps - first_zero_dist) // self.length

    def go_left(self, index, steps):
        return (index - steps) % self.length

    def go_left_time(self, index, steps):
        # how many times do we cross index 0 going left by `steps` from `index`?
        if steps == 0:
            return 0
        first_zero_dist = self.length if index == 0 else index
        if steps < first_zero_dist:
            return 0
        return 1 + (steps - first_zero_dist) // self.length


a = []
while True:
    b = input()
    if not b:
        break
    a.append(b)

arr = [x for x in range(100)]
sol = Solution(arr)
start_index = 50

# --- Part 1: final position after all moves ---
pos = start_index
for move in a:
    if move[0] == 'R':
        pos = sol.go_right(pos, int(move[1:]))
    elif move[0] == 'L':
        pos = sol.go_left(pos, int(move[1:]))
# print(pos)   # uncomment for Part 1

# --- Part 2: count how many times index 0 is crossed ---
head = 0
count = 0
start_index = 50  # reset for Part 2

while head < len(a):
    if a[head][0] == 'R':
        steps = int(a[head][1:])
        count += sol.go_right_time(start_index, steps)
        start_index = sol.go_right(start_index, steps)
    elif a[head][0] == 'L':
        steps = int(a[head][1:])
        count += sol.go_left_time(start_index, steps)
        start_index = sol.go_left(start_index, steps)
    head += 1

print(count)
