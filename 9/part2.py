#!/usr/bin/env python3

moves: list[tuple[str, int]]
with open('input') as f:
    lines = [l.rstrip().split() for l in f.readlines()]
    moves = [(l[0], int(l[1])) for l in lines]

chain = 10 * [(0, 0)]
tail_visited = set()
for direction, num_steps in moves:
    while num_steps:
        x, y = chain[0]
        if direction == 'U':
            chain[0] = (x, y + 1)
        elif direction == 'D':
            chain[0] = (x, y - 1)
        elif direction == 'R':
            chain[0] = (x + 1, y)
        elif direction == 'L':
            chain[0] = (x - 1, y)

        for i in range(1, 10):
            x0, y0 = chain[i]
            x1, y1 = chain[i-1]
            if abs(x0 - x1) > 1 or abs(y0 - y1) > 1: # if not touching
                def sign(n: int) -> int:
                    if n > 0: return 1
                    elif n < 0: return -1
                    else: return 0

                chain[i] = (x0 + sign(x1 - x0), y0 + sign(y1 - y0))

        tail_visited.add(chain[-1])
        num_steps -= 1

print(len(tail_visited))

