#!/usr/bin/env python3

from os.path import dirname, realpath, join
from itertools import cycle
from collections import defaultdict


def transform_input(input_):
    input_ = input_.splitlines()
    # custom transform for the day

    return int(input_[0])


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        input_ = f.read()

    input_ = transform_input(input_)

    return input_


def move_right(x, y):
    return x + 1, y


def move_down(x, y):
    return x, y - 1


def move_left(x, y):
    return x - 1, y


def move_up(x, y):
    return x, y + 1


def gen_spiral_points(n):
    moves = cycle([move_right, move_up, move_left, move_down])
    num = 1
    pos = (0, 0)
    num_steps = 1

    yield num, pos

    while True:
        for _ in range(2):
            move = next(moves)
            for _ in range(num_steps):
                if num >= n:
                    return
                pos = move(*pos)
                num += 1

                yield num, pos
        num_steps += 1


def solve_part1(input_):
    points = gen_spiral_points(input_)
    for point in points:
        pass

    dist = abs(point[1][0]) + abs(point[1][1])
    print(dist)


def get_neighbours_sum(points_map, point):
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbours.append((i, j))

    s = 0
    for neighbour in neighbours:
        neighbour_point = (point[0] + neighbour[0], point[1] + neighbour[1])
        s += points_map[neighbour_point]

    return s


def solve_part2(input_):
    points = gen_spiral_points(input_)
    points_map = defaultdict(int)
    points_map[(0, 0)] = 1
    for point in points:
        neighbours_sum = get_neighbours_sum(points_map, point[1])
        if neighbours_sum > input_:
            print(neighbours_sum)
            break
        points_map[point[1]] = neighbours_sum


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == "__main__":
    main()
