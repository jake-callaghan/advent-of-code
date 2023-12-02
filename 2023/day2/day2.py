from core.decorators import *


def parse_game(x):
    def parse_round(x):
        """4 red, 8 green, 12 blue -> {red: 4, green: 8, blue: 12} """
        round = {}
        vs = x.split(', ')
        for v in vs:
            ss = v.split(' ')
            round[ss[1]] = int(ss[0])
        return round

    xs = x.strip().split(': ')
    return {
        'id': int(xs[0].split(' ')[-1]),
        'rounds': [parse_round(r) for r in xs[1].split('; ')]
    }


@print_output
@test(filename='part1_example.txt', output=8)
def part_one(lines):
    total = 0
    for line in lines:
        game = parse_game(line)
        ok = True
        for round in game['rounds']:
            if round.get('red', 0) > 12 or round.get('blue', 0) > 14 or round.get('green', 0) > 13:
                ok = False
                break
        if ok:
            total += game['id']
    return total


@print_output
@test(filename='part1_example.txt', output=2286)
def part_two(lines):
    total = 0
    for line in lines:
        game = parse_game(line)
        m = {'red': 0, 'blue': 0, 'green': 0}
        for r in game['rounds']:
            for c in ['red', 'green', 'blue']:
                if c in r:
                    m[c] = max(m[c], r[c])
        total += m['red'] * m['blue'] * m['green']
    return total


if __name__ == '__main__':
    day2_input = readfile('input.txt')
    part_one(day2_input)
    part_two(day2_input)
