#!/usr/bin/env python3

elvesCals = []
with open('input') as f:
    currCals = 0
    for line in f.readlines():
        line = line.rstrip()

        if line == '':
            elvesCals.append(currCals)
            currCals = 0
        else:
            currCals += int(line)

topThree = sorted(elvesCals)[-3:]

print(topThree)
print(sum(topThree))
