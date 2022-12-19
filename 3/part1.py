#!/usr/bin/env python3

totalPriority = 0
with open('input') as f:
    for items in [l.rstrip() for l in f.readlines()]:
        firstHalf = set(items[:len(items) // 2])
        secondHalf = set(items[len(items) // 2:])
        mistake = firstHalf.intersection(secondHalf).pop()

        if mistake.isupper():
            totalPriority += ord(mistake) - ord('A') + 27
        else:
            totalPriority += ord(mistake) - ord('a') + 1

print(f'{totalPriority=}')
