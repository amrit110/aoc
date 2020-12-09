#!/usr/bin/env python3

from os.path import dirname, realpath, join


def transform_input(input_):
    # custom transform for the day

    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        input_ = f.read()

    input_ = transform_input(input_)

    return input_


def solve_part1(input_):
    floor = 0
    for s in input_:
        if s == "(":
            floor += 1
        elif s == ")":
            floor -= 1

    print(floor)


def solve_part2(input_):
    floor = 0
    for i, s in enumerate(input_):
        if s == "(":
            floor += 1
        elif s == ")":
            floor -= 1

        if floor == -1:
            print(i + 1)
            break


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == "__main__":
    main()
