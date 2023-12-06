from core.decorators import print_output, test
from core.utils import readfile


def parse_input(filename):
    f = lambda i: [int(t) for t in readfile(filename)[i].split(' ')[1:] if t != '']
    return zip(f(0), f(1))


@print_output
@test('part1_example.txt', 288, parser=parse_input)
@test('part2_example.txt', 71503, parser=parse_input)
def part_one(data):
    total = 1
    for time, record in data:
        n = 0
        for t in range(time - 1, 0, -1):
            d = t * (time - t)
            if d > record:
                n += 1
        total *= n
    return total


if __name__ == '__main__':
    part_one('input.txt')
    part_one('part2_input.txt')
