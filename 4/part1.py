#!/usr/bin/env python3

numInside = 0
with open('input') as f:
    for team in [l.split(',') for l in f.readlines()]:
        firstRange =  [int(n) for n in team[0].split('-')]
        secondRange = [int(n) for n in team[1].split('-')]
        A, B = firstRange
        C, D = secondRange

        inside = False
        if A <= C:
            if D <= B:
                inside = True
        else:
            if B <= D:
                inside = True

        numInside += 1 if inside else 0

print(f'{numInside=}')
