#!/usr/bin/env python3

grid: list[list[tuple[int, bool]]]
with open('input') as f:
    grid = [[(int(c), False) for c in l.rstrip()] for l in f.readlines()]

N = len(grid)

# row-by-row
for rownum in range(N):
    # from the left
    tallest = -1
    for colnum in range(N):
        height, isvisible = grid[rownum][colnum]
        grid[rownum][colnum] = (height, isvisible or height > tallest)
        tallest = max(tallest, height)

    # from the right
    tallest = -1
    for colnum in range(N - 1, -1, -1):
        height, isvisible = grid[rownum][colnum]
        grid[rownum][colnum] = (height, isvisible or height > tallest)
        tallest = max(tallest, height)

# col-by-col
for colnum in range(N):
    # from the top
    tallest = -1
    for rownum in range(N):
        height, isvisible = grid[rownum][colnum]
        grid[rownum][colnum] = (height, isvisible or height > tallest)
        tallest = max(tallest, height)

    # from the bottom
    tallest = -1
    for rownum in range(N - 1, -1, -1):
        height, isvisible = grid[rownum][colnum]
        grid[rownum][colnum] = (height, isvisible or height > tallest)
        tallest = max(tallest, height)

print(sum([1 for row in grid for cell in row if cell[1]]))

