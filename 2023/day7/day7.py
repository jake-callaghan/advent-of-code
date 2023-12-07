import collections
from functools import lru_cache

from core.decorators import print_output, test
from core.utils import readfile


@lru_cache
def parse_input(filename, replacements={'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}):
    out = []
    def replace(c):
        if c in replacements: return replacements[c]
        return int(c)

    for line in readfile(filename):
        cards = [replace(c) for c in line[0:5]]
        bid = int(line[6:])
        counts = collections.Counter(cards)
        num_unique_cards = len(counts.keys())
        if num_unique_cards == 1:  # 5 of a kind
            strength = 7
        elif num_unique_cards == 2:  # either 4 of a kind or full house
            count = list(counts.values())[0]
            strength = 6 if count == 1 or count == 4 else 5
        elif num_unique_cards == 3:  # either 3 of a kind, 2 pair
            count = max(counts.values())
            strength = 4 if count == 3 else 3
        elif num_unique_cards == 4:  # 1 pair
            strength = 2
        else:  # high card
            strength = 1
        out.append((strength, cards, bid))
    return out


@print_output
@test(filename='part1_example.txt', expected_output=6440, parser=parse_input)
def part_one(data):
    score = 0
    sorted_hands = sorted(data, key=lambda x: (x[0], x[1]))
    for rank, hand in enumerate(sorted_hands):
        score += (rank + 1) * hand[2]
    return score


if __name__ == '__main__':
    data = parse_input('input.txt')
    print(data)
    part_one(data)
