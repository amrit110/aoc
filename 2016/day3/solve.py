#!/usr/bin/env python3

from os.path import dirname, realpath, join


def transform_input(input_):
    # custom transform for the day
    input_ = [int(num) for num in input_.split()]

    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def solve_part1(input_):
    num_valid = 0
    for sides in input_:
        sides = sorted(sides)
        if sides[0] + sides[1] > sides[2]:
            num_valid += 1

    print(num_valid)


def solve_part2(input_):
    num_valid = 0
    nums_list = []
    for nums in input_:
        nums_list.append(nums)

    num_nums = len(nums_list)
    for i in range(0, num_nums, 3):
        triangles = list(zip(*nums_list[i : i + 3]))
        for triangle in triangles:
            triangle = sorted(triangle)
            if triangle[0] + triangle[1] > triangle[2]:
                num_valid += 1

    print(num_valid)


def main():
    solve_part1(read_input())
    solve_part2(read_input())


if __name__ == "__main__":
    main()
