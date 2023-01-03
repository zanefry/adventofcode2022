#!/usr/bin/env python3

from math import floor

held_items: list[list[int]]
operations: list[tuple[str, str]]
divisors: list[int]
options: list[tuple[int, int]]
with open('input') as f:
    monkeys = [[l.lstrip() for l in block.split('\n')] for block in f.read().split('\n\n')]

    held_items = []
    operations = []
    divisors = []
    options = []
    for monkey in monkeys:
        # starting list
        held_items.append([int(n) for n in monkey[1].split(': ')[1].split(', ')])

        # operation
        op, right = monkey[2].split()[-2:]
        operations.append((op, right))

        # test divisor
        divisors.append(int(monkey[3].split()[-1]))

        # test options
        iftrue = int(monkey[4].split()[-1])
        iffalse = int(monkey[5].split()[-1])
        options.append((iftrue, iffalse))

modulus = 1
for d in divisors:
    modulus *= d

inspection_counts = 8 * [0]
for round in range(1, 10001):
    for monkey in range(8):
        op, val = operations[monkey]
        divisor = divisors[monkey]
        iftrue, iffalse = options[monkey]

        while held_items[monkey]:
            item = held_items[monkey].pop(0)
            inspection_counts[monkey] += 1

            if op == '+':
                if val == 'old':
                    item += item
                else:
                    item += int(val)
            elif op == '*':
                if val == 'old':
                    item *= item
                else:
                    item *= int(val)

            item %= modulus

            dest = iftrue if item % divisor == 0 else iffalse
            held_items[dest].append(item)

top1, top2 = sorted(inspection_counts)[-2:]
print(top1 * top2)
