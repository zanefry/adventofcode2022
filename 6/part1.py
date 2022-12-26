#!/usr/bin/env python3

sequence: str
with open('input') as f:
    sequence = f.read().rstrip()

numDistinct = 4

length = numDistinct
for i in range(numDistinct, len(sequence)):
    lastFour = sequence[i - numDistinct:i]

    if len(set(lastFour)) == numDistinct:
        break

    length += 1

print(length)
