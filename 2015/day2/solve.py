#!/usr/bin/env python3

from os.path import dirname, realpath, join


def transform_input(input_):
    input_ = input_.splitlines()
    # custom transform for the day
    dimensions = []
    for line in input_:
        l, w, h = line.split("x")
        dimensions.append(tuple(map(int, (l, w, h))))

    return dimensions


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        input_ = f.read()

    input_ = transform_input(input_)

    return input_


def solve_part1(input_):
    sa = 0
    for (l, w, h) in input_:
        sa += 2 * (l * w + w * h + h * l) + min((l * w, w * h, h * l))

    print(sa)


def solve_part2(input_):
    ribbon_length = 0
    for (l, w, h) in input_:
        ribbon_length += 2 * sum(sorted([l, w, h])[0:2]) + l * w * h

    print(ribbon_length)


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == "__main__":
    main()
