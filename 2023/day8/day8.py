from functools import lru_cache

import numpy as np

from core.decorators import print_output, test
from core.utils import readfile


@lru_cache
def parse_input(filename):
    lines = readfile(filename)
    steps = lines[0]
    nodes = {}
    for line in lines[2:]:
        nodes[line[0:3]] = (line[7:10], line[12:15])
    return {
        'steps': steps,
        'nodes': nodes
    }


def part_one(data, start='AAA', terminal=lambda x: x == 'ZZZ'):
    count = 0
    current = start
    while not terminal(current):
        for step in data['steps']:
            options = data['nodes'][current]
            current = options[0] if step == 'L' else options[1]
            count += 1
            if terminal(current):
                return count
    return count


@print_output
@test(filename='part2_example.txt', expected_output=6, parser=parse_input)
def part_two(data):
    return np.lcm.reduce([part_one(data, start=n, terminal=lambda x: x[-1] == 'Z') for n in data['nodes'] if n[-1] == 'A'])


if __name__ == '__main__':
    print(part_one(parse_input('input.txt')))
    part_two(parse_input('input.txt'))
