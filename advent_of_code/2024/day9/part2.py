# Advent of Code 2024 - Day 9: Disk Fragmenter
# Part 2 - Move whole files at once into leftmost fitting free space
#
# QUESTION:
# Same disk map as Part 1.
# Now instead of moving individual blocks, move WHOLE FILES at once.
# Starting from the highest file ID and going down:
#   Try to move the file to the leftmost free span that fits it AND is to its left.
#   If no such span exists, the file stays in place.
#
# Checksum = same formula: sum of (position * file_id) for every file block.
#
# APPROACH:
# Track file positions as (start, length) and free spans as (start, length).
# For each file from highest to lowest ID, find the first free span to its left
# that fits. If found, move it there and update the free span list.

import sys

disk_map = sys.stdin.read().strip()

# build file list: [(start, length)] indexed by file_id
# and free spans: [(start, length)]
files = {}
free_spans = []
pos = 0
file_id = 0

for i, ch in enumerate(disk_map):
    length = int(ch)
    if i % 2 == 0:
        files[file_id] = (pos, length)
        file_id += 1
    else:
        if length > 0:
            free_spans.append([pos, length])
    pos += length

# process files from highest id down to 0
for fid in range(file_id - 1, -1, -1):
    f_start, f_len = files[fid]

    # find leftmost free span that fits this file AND is before the file's current position
    best = None
    for i, (s_start, s_len) in enumerate(free_spans):
        if s_start >= f_start:
            break  # only look left of current position
        if s_len >= f_len:
            best = i
            break

    if best is not None:
        s_start, s_len = free_spans[best]
        # move the file here
        files[fid] = (s_start, f_len)
        # shrink or remove the free span we just used
        if s_len == f_len:
            free_spans.pop(best)
        else:
            free_spans[best][0] += f_len
            free_spans[best][1] -= f_len

# compute checksum from final file positions
checksum = 0
for fid, (start, length) in files.items():
    for offset in range(length):
        checksum += (start + offset) * fid

print(checksum)
