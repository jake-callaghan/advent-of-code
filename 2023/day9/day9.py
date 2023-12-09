from functools import lru_cache
import numpy as np
from core.decorators import print_output, test
from core.utils import readfile


def expand(xss):
    while np.any(xss[-1]):
        xss += [[b - a for a, b in zip(xss[-1], xss[-1][1:])]]
    head, tail = 0, 0
    for i in range(len(xss) - 1, -1, -1):
        xss[i].append(tail := tail + xss[i][-1])  # part 1
        xss[i].insert(0, head := xss[i][0] - head)  # part 2
    return xss


@lru_cache
def parse_input(filename):
    xss = []
    for line in readfile(filename):
        xss.append(expand([[int(x) for x in line.split(' ')]]))
    return xss


@print_output
@test(filename='example.txt', expected_output=114, parser=parse_input)
def part_one(data):
    return sum([xs[0][-1] for xs in data])


@print_output
@test(filename='example2.txt', expected_output=5, parser=parse_input)
def part_two(data):
    return sum([xs[0][0] for xs in data])


if __name__ == '__main__':
    data = parse_input('input.txt')
    part_one(data)
    part_two(data)
