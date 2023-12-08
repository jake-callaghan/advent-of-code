from functools import lru_cache

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


@print_output
@test(filename='part1_example.txt', expected_output=6, parser=parse_input)
def part_one(data):
    count = 0
    current = 'AAA'
    while current != 'ZZZ':
        for step in data['steps']:
            options = data['nodes'][current]
            current = options[0] if step == 'L' else options[1]
            count += 1
            if current == 'ZZZ':
                return count
    return count


@print_output
@test(filename='part2_example.txt', expected_output=6, parser=parse_input)
def part_two(data):
    count = 0
    current = [n for n in data['nodes'] if n[-1] == 'A']

    def done():
        for n in current:
            if n[-1] != 'Z':
                return False
        return True

    while not done():
        for step in data['steps']:
            current = [data['nodes'][n][0] if step == 'L' else data['nodes'][n][1] for n in current]
            count += 1
            if count % 100000 == 0:
                print(f"Steps: {count}")
            if done():
                return count
    return count


if __name__ == '__main__':
    part_one(parse_input('input.txt'))
    part_two(parse_input('input.txt'))
