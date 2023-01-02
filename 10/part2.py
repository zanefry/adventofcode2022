#!/usr/bin/env python3

instructions: list[tuple[str, int]]
with open('input') as f:
    lines = [l.rstrip().split() for l in f.readlines()]
    instructions = [(l[0], int(l[1])) if len(l) == 2 else (l[0], 0) for l in lines]

X = 1
cycle = 1
changes = []
for op, val in instructions:
    X += val

    if op == 'addx':
        cycle += 2
        changes.append((cycle, X))
    else:
        cycle += 1

change_idx = 0
for cycle in range(1, 241):
    change_cycle, change_X = changes[change_idx]

    X: int
    if cycle < change_cycle: # before first change
        X = 1
    elif change_idx == len(changes) - 1: # after last change
        X = change_X
    else:
        if cycle == changes[change_idx + 1][0]: # next change hit
            change_idx += 1

        X = changes[change_idx][1]

    pixel = (cycle - 1) % 40
    if X - 1 <= pixel <= X + 1:
        print('#', end='')
    else:
        print('.', end='')

    if cycle % 40 == 0:
        print()
