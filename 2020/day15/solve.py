#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time
from itertools import count
from collections import defaultdict


def transform_input(input_):
    input_ = input_.strip()
    # custom transform for the day

    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "test_input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def get_nth_spoken(input_, n):
    input_ = next(input_).split(",")
    input_ = [int(n) for n in input_]
    input_sz = len(input_)
    mem = defaultdict(list)
    for i in count(1):
        if i <= input_sz:
            new_spoken = input_[i - 1]
        elif len(mem[last_spoken]) == 1:
            new_spoken = 0
        else:
            new_spoken = mem[last_spoken][-1] - mem[last_spoken][-2]
        if i == n:
            return new_spoken
        mem[new_spoken].append(i)
        last_spoken = new_spoken


def solve_part1(input_):
    print(get_nth_spoken(input_, 2020))


def solve_part2(input_):
    print(get_nth_spoken(input_, 30000000))


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
