#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time


directions = {"E": 1, "W": -1, "N": 1j, "S": -1j}
rotations = {"L": 1j, "R": -1j}


def transform_input(input_):
    input_ = input_.strip()
    # custom transform for the day

    return input_[0], int(input_[1:])


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def solve_part1(input_):
    ship_direction = 1
    ship_position = 0
    for action, value in input_:
        if action in directions:
            ship_position += directions[action] * value
        elif action in rotations:
            ship_direction *= rotations[action] ** (value // 90)
        else:
            ship_position += ship_direction * value
    print(int(abs(ship_position.real) + abs(ship_position.imag)))


def solve_part2(input_):
    waypoint = 10 + 1j
    ship_position = 0
    for action, value in input_:
        if action in directions:
            waypoint += directions[action] * value
        elif action in rotations:
            waypoint *= rotations[action] ** (value // 90)
        else:
            ship_position += waypoint * value
    print(int(abs(ship_position.real) + abs(ship_position.imag)))


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
