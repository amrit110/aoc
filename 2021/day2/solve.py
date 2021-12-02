#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time


def transform_input(input_):
    input_ = input_.strip()
    # custom transform for the day

    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def solve_part1(input_):
    hp, dep = 0, 0
    for line in input_:
        dir_, steps = line.split(" ")
        steps = int(steps)
        if dir_ == "forward":
            hp += steps
        elif dir_ == "up":
            dep -= steps
        elif dir_ == "down":
            dep += steps
    print(hp * dep)


def solve_part2(input_):
    hp, dep, aim = 0, 0, 0
    for line in input_:
        dir_, steps = line.split(" ")
        steps = int(steps)
        if dir_ == "forward":
            hp += steps
            dep += aim * steps
        elif dir_ == "up":
            aim -= steps
        elif dir_ == "down":
            aim += steps
    print(hp * dep)


def main():
    start_time = time.time()
    solve_part1(read_input())
    elapsed_time = (time.time() - start_time) * 1e3
    print(f"Time elapsed for part 1: {elapsed_time} ms")

    start_time = time.time()
    solve_part2(read_input())
    elapsed_time = (time.time() - start_time) * 1e3
    print(f"Time elapsed for part 2: {elapsed_time} ms")


if __name__ == "__main__":
    main()
