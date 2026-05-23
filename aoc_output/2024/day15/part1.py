# Advent of Code 2024 - Day 15: Warehouse Woes
# Part 1 - Simulate robot pushing boxes in a warehouse
#
# QUESTION:
# Grid has walls '#', boxes 'O', robot '@', empty '.'.
# The robot follows a sequence of moves (^v<>).
# When the robot tries to move into a box, it pushes it.
# A chain of boxes all get pushed if there's empty space behind them.
# If there's a wall at the end of the chain, nothing moves.
#
# GPS coordinate of a box = 100 * row + col.
# Return sum of GPS coordinates of all boxes after all moves.
#
# APPROACH:
# Simulate each move. When moving into a box, scan ahead to find where the
# chain ends — if empty space found, shift everything one step.

import sys

data = sys.stdin.read().split('\n\n')
grid = [list(line) for line in data[0].splitlines()]
moves = data[1].replace('\n', '')

ROWS, COLS = len(grid), len(grid[0])
dir_map = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}

# find robot start
r, c = next((r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == '@')

for move in moves:
    dr, dc = dir_map[move]
    nr, nc = r + dr, c + dc
    cell = grid[nr][nc]

    if cell == '#':
        continue  # wall — don't move

    if cell == '.':
        # empty — just move
        grid[r][c] = '.'
        grid[nr][nc] = '@'
        r, c = nr, nc

    elif cell == 'O':
        # find end of the chain of boxes
        er, ec = nr, nc
        while grid[er][ec] == 'O':
            er += dr
            ec += dc
        if grid[er][ec] == '#':
            continue  # wall at end of chain — nothing moves
        # shift: put box at the end, robot moves forward
        grid[er][ec] = 'O'
        grid[nr][nc] = '@'
        grid[r][c] = '.'
        r, c = nr, nc

# sum GPS coordinates of all boxes
total = sum(100*r + c for r in range(ROWS) for c in range(COLS) if grid[r][c] == 'O')
print(total)
