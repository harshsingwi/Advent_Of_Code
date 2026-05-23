# Advent of Code 2024 - Day 9: Disk Fragmenter
# Part 1 - Compact the disk by moving individual file blocks, then checksum
#
# QUESTION:
# The input is a dense "disk map" — alternating digits representing:
#   file_length, free_space, file_length, free_space, ...
# File IDs start at 0. So "12345" means:
#   file 0 takes 1 block, 2 free blocks, file 1 takes 3 blocks, 4 free, file 2 takes 5 blocks
#
# Compact by moving individual file blocks from the END of the disk into the
# leftmost available free space, one block at a time.
#
# Checksum = sum of (position * file_id) for every file block.
#
# APPROACH:
# Expand the disk map into a flat list of block contents (file id or None for free).
# Use two pointers: left scans for free space, right scans for file blocks from the end.
# Swap until they meet.

import sys

disk_map = sys.stdin.read().strip()

# expand disk map into block list: [0,0,None,None,1,1,1,...] etc.
blocks = []
file_id = 0
for i, ch in enumerate(disk_map):
    length = int(ch)
    if i % 2 == 0:
        blocks.extend([file_id] * length)
        file_id += 1
    else:
        blocks.extend([None] * length)

# two-pointer compact: move blocks from right into free space from left
left = 0
right = len(blocks) - 1

while left < right:
    while left < right and blocks[left] is not None:
        left += 1  # find next free slot from left
    while left < right and blocks[right] is None:
        right -= 1  # find next file block from right
    if left < right:
        blocks[left], blocks[right] = blocks[right], blocks[left]

# compute checksum
checksum = 0
for pos, block in enumerate(blocks):
    if block is not None:
        checksum += pos * block

print(checksum)
