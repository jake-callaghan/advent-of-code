from core.decorators import print_output, test
from core.utils import readfile


@print_output
@test('part1_example.txt', 288)
@test('part2_example.txt', 71503)
def part_one(lines):
    total = 1
    for time, record in parse_input(lines):
        n = 0
        for t in range(time - 1, 0, -1):
            d = t * (time - t)
            if d > record:
                n += 1
        total *= n
    return total


def parse_input(lines):
    f = lambda i: [int(t) for t in lines[i].split(' ')[1:] if t != '']
    return zip(f(0), f(1))


if __name__ == '__main__':
    part_one(readfile('input.txt'))
    part_one(readfile('part2_input.txt'))
