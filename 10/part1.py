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

score = 0
check_cycle = 20
for i, change in enumerate(changes[:-1]):
    curr_cycle, X = change
    next_cycle, _ = changes[i+1]
    if curr_cycle <= check_cycle < next_cycle:
        score += check_cycle * X
        check_cycle += 40

print(score)
