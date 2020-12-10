#!/usr/bin/env python3

from os.path import dirname, realpath, join
from collections import defaultdict
import time


def transform_input(input_):
    # custom transform for the day

    return int(input_)


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def solve_part1(input_):
    rating = 0
    joltages = sorted(list([v for v in input_]))
    num_1_diffs, num_3_diffs = 0, 0

    for jo in joltages:
        if jo - rating == 1:
            num_1_diffs += 1
        elif jo - rating == 3:
            num_3_diffs += 1
        rating = jo
    num_3_diffs += 1

    print(num_1_diffs * num_3_diffs)


def count_num_paths(joltages):
    paths = defaultdict(int)
    paths[joltages[1]] = 1
    end_idx = len(joltages)

    for i in range(1, len(joltages) - 1):
        jo_curr = joltages[i]
        j = 1
        while joltages[i] - joltages[i + j] <= 3:
            jo_next = joltages[i + j]
            paths[jo_next] += paths[jo_curr]
            j += 1
            if (i + j) == end_idx:
                break

    return paths[0]


def solve_part2(input_):
    joltages = sorted(list([v for v in input_]))[::-1] + [0]
    joltages = [joltages[0] + 3] + joltages
    num_paths = count_num_paths(joltages)

    print(num_paths)


def main():
    start_time = time.time()
    solve_part1(read_input())
    elapsed_time = (time.time() - start_time) * 1e3
    print(f"Time elapsed: {elapsed_time} ms")
    start_time = time.time()
    solve_part2(read_input())
    elapsed_time = (time.time() - start_time) * 1e3
    print(f"Time elapsed: {elapsed_time} ms")


if __name__ == "__main__":
    main()
