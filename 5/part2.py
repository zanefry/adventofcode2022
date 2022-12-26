#!/usr/bin/env python3

state: list[str]
moveLines: list[str]
with open('input') as f:
    lines = [l.rstrip() for l in f.readlines()]
    state = lines[:lines.index('')]
    moveLines = lines[lines.index('') + 1:]

# Parse columns

numCols = len(state[-1].split())

cols = []
for i in range(numCols):
    cols.append([row[1 + 4*i] for row in reversed(state)])
    cols[i] = [s for s in cols[i][1:] if s != ' '] # remove column number and spaces

# Parse moves

moves = []
for line in moveLines:
    moves.append([int(c) for c in line.split() if c.isdecimal()])

# Do moves

for numBoxes, srcCol, dstCol in moves:
    srcCol, dstCol = srcCol - 1, dstCol - 1 # they index from 1

    moved = cols[srcCol][-numBoxes:]
    cols[srcCol] = cols[srcCol][:-numBoxes]
    cols[dstCol].extend(moved)

print(''.join([col[-1] for col in cols]))
