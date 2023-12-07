import math
from functools import lru_cache

from core.decorators import test, print_output
from core.utils import readfile


@lru_cache
def parser(filename):
    out = []
    for line in readfile(path=filename):
        vs1 = line.split(': ')
        vs2 = vs1[1].split(' | ')
        card = {
            'id': int(vs1[0].split(' ')[-1]),
            'winners': {int(x.strip()) for x in vs2[0].split(' ') if x != ''},
            'values': {int(x.strip()) for x in vs2[1].split(' ') if x != ''}
        }
        card['number_of_winners'] = len(card['winners'] & card['values'])
        out.append(card)
    return out


@print_output
@test('part1_example.txt', 13, parser)
def part_one(data):
    score = 0
    for card in data:
        n = card['number_of_winners']
        score += 0 if n == 0 else math.pow(2, n - 1)
    return score


@print_output
@test('part1_example.txt', 30, parser)
def part_two(data):
    copies = {}  # copies[i] = # of copies of card i we have
    for i, card in enumerate(data):
        id = card['id']
        if id not in copies:
            copies[id] = 1
        for n in range(1, card['number_of_winners'] + 1):
            copies[id + n] = copies.get(id + n, 1) + copies[id]
    return sum(copies.values())


if __name__ == '__main__':
    data = parser('input.txt')
    part_one(data)
    part_two(data)
