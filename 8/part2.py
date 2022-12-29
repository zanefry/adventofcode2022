#!/usr/bin/env python3

grid: list[list[tuple[int, int]]]
with open('input') as f:
    grid = [[(int(c), 0) for c in l.rstrip()] for l in f.readlines()]

finalscores = []
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        scores = [0, 0, 0, 0]
        srcheight, _ = cell

        # right
        dj = 1
        while j + dj < len(grid):
            scores[0] += 1
            height = grid[i][j + dj][0]

            if srcheight <= height:
                break

            dj += 1

        # left
        dj = -1
        while j + dj >= 0:
            scores[1] += 1
            height = grid[i][j + dj][0]

            if srcheight <= height:
                break

            dj -= 1

        # down
        di = 1
        while i + di < len(grid):
            scores[2] += 1
            height = grid[i + di][j][0]

            if srcheight <= height:
                break

            di += 1

        # up
        di = -1
        while i + di >= 0:
            scores[3] += 1
            height = grid[i + di][j][0]

            if srcheight <= height:
                break

            di -= 1

        finalscore = 1
        for score in scores:
            finalscore *= score

        finalscores.append(finalscore)

print(max(finalscores))
