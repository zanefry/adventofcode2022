#!/usr/bin/env python3

from queue import PriorityQueue

grid: list[list[int]]
end: tuple[int, int]
with open('input') as f:
    letters = [list(l.rstrip()) for l in f.readlines()]
    for y, row in enumerate(letters):
        if 'S' in row:
            x = row.index('S')
            letters[y][x] = 'a'
        if 'E' in row:
            x = row.index('E')
            end = (x, y)
            letters[y][x] = 'z'

    grid = [[ord(c) - ord('a') for c in row] for row in letters]

COLSIZE = len(grid)
ROWSIZE = len(grid[0])

def search(start: tuple[int, int], end: tuple[int, int]):
    def dist(a: tuple[int, int], b: tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def neighbors(node: tuple[int, int]) -> list[tuple[int, int]]:
        xs = [1, 0, -1, 0]
        ys = [0, 1, 0, -1]

        neighbors = []
        x, y = node
        for i in range(4):
            dx, dy = xs[i], ys[i]
            if 0 <= x + dx < ROWSIZE and 0 <= y + dy < COLSIZE:
                if grid[y + dy][x + dx] <= grid[y][x] + 1:
                    neighbors.append((x + dx, y + dy))

        return neighbors


    last_node = {} # maps node -> prev node

    perimeter = PriorityQueue()
    perimeter.put((0, start))

    # set default val to 1000
    gscore = {}
    fscore = {}
    in_perimeter = {}
    for y in range(COLSIZE):
        for x in range(ROWSIZE):
            gscore[repr((x, y))] = 1000
            fscore[repr((x, y))] = 1000
            in_perimeter[repr((x, y))] = False

    gscore[repr(start)] = 0
    fscore[repr(start)] = dist(start, end)
    in_perimeter[repr(start)] = True

    while not perimeter.empty():
        _, current = perimeter.get()
        in_perimeter[repr(current)] = False

        if current == end:
            return last_node

        for neighbor in neighbors(current):
            tentative_gscore = gscore[repr(current)] + 1
            if tentative_gscore < gscore[repr(neighbor)]:
                last_node[repr(neighbor)] = current
                gscore[repr(neighbor)] = tentative_gscore
                fscore[repr(neighbor)] = tentative_gscore + dist(neighbor, end)

                if not in_perimeter[repr(neighbor)]:
                    perimeter.put((fscore[repr(neighbor)], neighbor))
                    in_perimeter[repr(neighbor)] = True

    return last_node

# get candidates
candidates = []
for y, row in enumerate(grid):
    for x, height in enumerate(row):
        if height == 0:
            candidates.append((x, y))

# get path lengths
path_lengths = []
for start in candidates:
    last_node = search(start, end)

    shortest_path = []
    current = end
    while repr(current) in last_node:
        current = last_node[repr(current)]
        shortest_path.append(current)

    path_lengths.append(len(shortest_path))

# print length of shortest
print(sorted([d for d in path_lengths if d])[0])
