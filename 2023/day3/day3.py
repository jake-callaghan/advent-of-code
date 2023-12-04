from functools import lru_cache

from core.decorators import *
from core.utils import *
from core.vector import Vector


@lru_cache
def parse(filename):
    numbers = []
    symbols = {}
    row = 0
    for line in readfile(filename):
        col = 0
        buffer = []
        while col < len(line):
            current = line[col]
            if current.isnumeric():
                buffer.append(Vector(row, col, int(current)))
            else:
                if len(buffer) > 0:
                    numbers.append(buffer)
                    buffer = []
                if current != '.':
                    if row not in symbols:
                        symbols[row] = {}
                    symbols[row][col] = current
            col += 1
        if len(buffer) > 0:
            numbers.append(buffer)
        row += 1
    return numbers, symbols


@print_output
@test(filename='part1_example.txt', expected_output=4361, parser=parse)
def part_one(data) -> int:
    total = 0
    ns, syms = data
    for n in ns:
        add = False
        for digit in n:
            for neighbor in digit.moore_neighborhood():
                if neighbor.i in syms and neighbor.j in syms[neighbor.i]:
                    add = True
                    break
            if add:
                break
        if add:
            total += int(''.join(map(str, [v.value for v in n])))
    return total


@print_output
@test(filename="part1_example.txt", expected_output=467835, parser=parse)
def part_two(data) -> int:
    total = 0
    nss, syms = data
    ns = {}
    # map points(i,j) to numbers covering points (i,j)
    for n in nss:
        value = int(''.join(map(str, [v.value for v in n])))
        for d in n:
            if d.i not in ns:
                ns[d.i] = {}
            ns[d.i][d.j] = value
    # find adjacent numbers to all * symbols
    for row in syms:
        for col in syms[row]:
            sym = syms[row][col]
            if sym != '*': continue
            ratios = set()
            for neighbor in Vector(row, col).moore_neighborhood():
                if neighbor.i in ns and neighbor.j in ns[neighbor.i]:
                    ratios.add(ns[neighbor.i][neighbor.j])

            if len(ratios) == 2:
                ratios_list = list(ratios)
                total += ratios_list[0] * ratios_list[1]
    return total


if __name__ == '__main__':
    data = parse('input.txt')
    part_one(data)
    part_two(data)
