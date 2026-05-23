# Advent of Code 2024 - Day 15: Warehouse Woes
# Part 2 - Wide warehouse: boxes are now 2 cells wide
#
# QUESTION:
# Scale the warehouse horizontally by 2:
#   # → ##    O → []    . → ..    @ → @.
# Now boxes are '[' and ']' pairs. Everything else is the same.
# Pushing vertically moves both halves of a box, which can fan out and push more boxes.
# GPS is still 100*row + col of the '[' character.
#
# APPROACH:
# Left/right pushes work similarly to Part 1 (scan ahead in a line).
# Up/down pushes require tracking the full "frontier" of box halves being pushed.
# Use BFS to find all boxes in the push chain, then move them all at once.

import sys
from collections import deque

data = sys.stdin.read().split('\n\n')
orig = data[0].splitlines()
moves = data[1].replace('\n', '')

# scale the map
scaled = []
for line in orig:
    row = ''
    for ch in line:
        if ch == '#': row += '##'
        elif ch == 'O': row += '[]'
        elif ch == '.': row += '..'
        elif ch == '@': row += '@.'
    scaled.append(list(row))

grid = scaled
ROWS, COLS = len(grid), len(grid[0])
dir_map = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}

r, c = next((r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == '@')

for move in moves:
    dr, dc = dir_map[move]
    nr, nc = r + dr, c + dc
    cell = grid[nr][nc]

    if cell == '#':
        continue

    if cell == '.':
        grid[r][c] = '.'
        grid[nr][nc] = '@'
        r, c = nr, nc

    elif cell in '[]':
        if dc != 0:
            # horizontal push — scan ahead for end of chain
            ec = nc
            while grid[nr][ec] in '[]':
                ec += dc
            if grid[nr][ec] == '#':
                continue
            # shift everything one step in move direction
            while ec != nc:
                grid[nr][ec] = grid[nr][ec - dc]
                ec -= dc
            grid[nr][nc] = '@'
            grid[r][c] = '.'
            r, c = nr, nc

        else:
            # vertical push — BFS to find all affected box halves
            # each box half drags along the other half of its box
            frontier = {(nr, nc)}
            if grid[nr][nc] == '[': frontier.add((nr, nc+1))
            else: frontier.add((nr, nc-1))

            all_boxes = set(frontier)
            q = deque(frontier)
            blocked = False

            while q and not blocked:
                br, bc = q.popleft()
                nbr = br + dr
                nbc = bc
                nch = grid[nbr][nbc]
                if nch == '#':
                    blocked = True
                    break
                if nch in '[]':
                    if (nbr, nbc) not in all_boxes:
                        all_boxes.add((nbr, nbc))
                        q.append((nbr, nbc))
                    # drag the other half of the box
                    other = (nbr, nbc+1) if nch == '[' else (nbr, nbc-1)
                    if other not in all_boxes:
                        all_boxes.add(other)
                        q.append(other)

            if blocked:
                continue

            # move all boxes in the push direction (top-to-bottom or bottom-to-top)
            sorted_boxes = sorted(all_boxes, key=lambda x: x[0], reverse=(dr > 0))
            for br, bc in sorted_boxes:
                grid[br + dr][bc] = grid[br][bc]
                grid[br][bc] = '.'

            grid[nr][nc] = '@'
            grid[r][c] = '.'
            r, c = nr, nc

total = sum(100*r + c for r in range(ROWS) for c in range(COLS) if grid[r][c] == '[')
print(total)
