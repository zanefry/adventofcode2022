#!/usr/bin/env python3

moves: list[tuple[str, int]]
with open('input') as f:
    lines = [l.rstrip().split() for l in f.readlines()]
    moves = [(l[0], int(l[1])) for l in lines]

head_pos = (0, 0)
tail_pos = head_pos
tail_visited = set()
for direction, num_steps in moves:
    while num_steps:
        prev_head_pos = head_pos

        x, y = head_pos
        if direction == 'U':
            head_pos = (x, y + 1)
        elif direction == 'D':
            head_pos = (x, y - 1)
        elif direction == 'R':
            head_pos = (x + 1, y)
        elif direction == 'L':
            head_pos = (x - 1, y)

        x, y = head_pos
        tx, ty = tail_pos
        if abs(x - tx) > 1 or abs(y - ty) > 1: # if tail not touching
            tail_pos = prev_head_pos

        tail_visited.add(tail_pos)
        num_steps -= 1

print(len(tail_visited))
