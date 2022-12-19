#!/usr/bin/env python3

totalPriority = 0
with open('input') as f:
    lines = [l.rstrip() for l in f.readlines()]
    groups = [lines[3*i:3*(i+1)] for i in range(len(lines) // 3)]

    for group in groups:
        sets = [set(line) for line in group]
        mistake = set.intersection(*sets).pop()

        if mistake.isupper():
            totalPriority += ord(mistake) - ord('A') + 27
        else:
            totalPriority += ord(mistake) - ord('a') + 1

print(f'{totalPriority=}')
