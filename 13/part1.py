#!/usr/bin/env python3

str_pairs: list[tuple[str, str]]
with open('dummyinput') as f:
    pieces = f.read().split('\n\n')
    str_pairs = [(l0.rstrip(), l1.rstrip()) for l0, l1 in [p.split() for p in pieces]]

def list_elements(s: str) -> list[str]:
    s = s[1:-1]
    if not s:
        return []

    elements = [[]]
    nest_level = 0
    for char in s:
        if nest_level == 0 and char == ',':
            elements.append([])
        else:
            elements[-1].append(char)

        if char == '[':
            nest_level += 1
        elif char == ']':
            nest_level -= 1

    return [''.join(e) for e in elements]

def parse_list(s: str) -> list:
    result = []
    for element in list_elements(s):
        if element[0] == '[':
            result.append(parse_list(element))
        else:
            result.append(int(element))

    return result

def compare_lists(left: list, right: list) -> bool:
    pass

# parse input into lists
pairs: list[tuple[list, list]]
pairs = [(parse_list(left), parse_list(right)) for left, right in str_pairs]

# recursively compare lists









