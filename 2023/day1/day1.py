from core.utils import *
from core.decorators import *


@print_output
@test('part1_example.txt', 142)
def part_one(lines):
    def parse_part_one(line) -> int:
        digits = [c for c in line if c.isnumeric()]
        return int(digits[0] + digits[-1])
    return sum([parse_part_one(line) for line in lines])


@print_output
@test('part2_example.txt', 281)
def part_two(lines):
    return sum([parse_part_two(line) for line in lines])


def parse_part_two(line) -> int:
    """Parse each line from left to right and right to left simultaneously"""
    def parse(subset, left_to_right):
        if len(subset) == 0:
            return None
        # either line[0..i) is a digit, or line[i-1] is a digit, or None
        for x in DIGITS:
            if x in subset:
                return DIGITS[x]

        c = subset[-1] if left_to_right else subset[0]
        if c.isnumeric():
            return int(c)
        return None

    i = 0
    first, last = None, None
    while i < len(line) and (first is None or last is None):
        if first is None:
            first = parse(line[0:i], True)
        if last is None:
            last = parse(line[(-i - 1):], False)
        i += 1
    return int(f"{first}{last}")


if __name__ == '__main__':
    lines = readfile('input.txt')
    part_one(lines)
    part_two(lines)
