import copy

from core.decorators import test, print_output
from core.vector import Vector
from core.utils import readfile, print_matrix


@print_output
@test(filename='part1_example.txt', output=13)
def part_one(lines) -> int:
    head = Vector(0, 0)
    tail = Vector(0, 0)
    seen = {tail}
    for line in lines:
        vs = line.split(' ')
        move = Vector.parse(vs[0])
        for i in range(0, int(vs[1])):
            head_prev = head.copy()
            head += move
            if head.real_distance(tail) > 2:
                # update tails location to head previous position
                tail = head_prev
                seen.add(tail)
    return len(seen)


@print_output
@test(filename='part2_example.txt', output=36)
def part_two(lines) -> int:
    rope = {i: Vector(0, 0, i) for i in range(0, 10)}
    rope[0].value = 'H'
    seen = {(rope[9].i, rope[9].j)}
    for line in lines:
        print(line)
        vs = line.split(' ')
        move = Vector.parse(vs[0])
        for i in range(0, int(vs[1])):
            seen.add((rope[9].i, rope[9].j))
            # move the head first
            rope_prev = copy.deepcopy(rope)
            rope[0] = rope[0] + move
            # now iterate over each knot to see if it's pulled into the preceding knots position
            for k in range(1, 10):
                leader = rope[k-1]
                knot = rope[k]
                if leader.real_distance(knot) > 2:
                    rope[k] = rope_prev[k-1]
                    rope[k].value = k
                else:
                    # can skip: no movement means the rest of the tail will stay still
                    break
        print(print_matrix(rope.values(), x_min=-30, x_max=30, y_min=-30, y_max=30))
    return len(seen)


if __name__ == '__main__':
    day9_input = readfile('input.txt')
    part_one(day9_input)
    part_two(day9_input)
