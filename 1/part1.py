#!/usr/bin/env python3

highestCals = 0
with open('input') as f:
    currCals = 0
    for line in f.readlines():
        line = line.rstrip()

        if line == '':
            highestCals = currCals if currCals > highestCals else highestCals
            currCals = 0
        else:
            currCals += int(line)

print(f'{highestCals=}')
