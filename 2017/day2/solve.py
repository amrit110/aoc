#!/usr/bin/env python3

from os.path import dirname, realpath, join


def transform_input(input_):
    input_ = input_.splitlines()
    # custom transform for the day
    spreadsheet = []
    for line in input_:
        spreadsheet.append([int(num) for num in line.split()])

    return spreadsheet


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        input_ = f.read()

    input_ = transform_input(input_)

    return input_


def solve_part1(input_):
    checksum = 0

    for nums in input_:
        smallest = min(nums)
        largest = max(nums)
        checksum += largest - smallest

    print(checksum)


def find_evenly_divisible(nums):
    sz = len(nums)
    for i in range(sz):
        for j in range(i + 1, sz):
            if nums[i] % nums[j] == 0:
                return int(nums[i] / nums[j])


def solve_part2(input_):
    checksum = 0

    for nums in input_:
        nums = sorted(nums)[::-1]
        checksum += find_evenly_divisible(nums)

    print(checksum)


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == "__main__":
    main()
