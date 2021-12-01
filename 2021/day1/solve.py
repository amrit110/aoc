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
    prev = None
    count = 0
    for num in input_:
        if prev is None:
            prev = int(num)
        if int(num) > prev:
            count += 1
        prev = int(num)
    print(count)


def solve_part2(input_):
    count = 0
    nums = [int(num) for num in input_]
    sums = [sum(nums[idx: idx + 3]) for idx in range(len(nums))]
    prev = None
    for s in sums:
        if prev is None:
            prev = s
        if s > prev:
            count += 1
        prev = s
    print(count)


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
