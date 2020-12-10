#!/usr/bin/env python3

from os.path import dirname, realpath, join


def transform_input(input_):
    # custom transform for the day

    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def solve_part1(input_):
    pass


def solve_part2(input_):
    pass


def main():
    solve_part1(read_input())
    solve_part2(read_input())


if __name__ == "__main__":
    main()
