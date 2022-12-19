#!/usr/bin/env python3

opponentOptions = ['A', 'B', 'C']
outcomes = ['X', 'Y', 'Z']

totalScore = 0
with open('input') as f:
    rounds = [l.split() for l in f.readlines()]
    for opsMove, result in rounds:
        opsMove = opponentOptions.index(opsMove)
        myMove = (opsMove - 1 + outcomes.index(result)) % 3

        totalScore += myMove + 1

        if opsMove != myMove:
            if (opsMove + 1) % 3 == myMove:
                totalScore += 6
        else:
            totalScore += 3

print(f'{totalScore=}')
