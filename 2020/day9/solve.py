#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time


def transform_input(input_):
    input_ = input_.splitlines()
    # custom transform for the day
    input_ = [int(num) for num in input_]

    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        input_ = f.read()

    input_ = transform_input(input_)

    return input_


def solve(input_):
    start_time = time.time()
    start = 0
    end = 25
    rem = len(input_[end:])
    for i in range(rem):
        preamble = input_[start:end]
        next_num = input_[end]
        valid = False
        for num in preamble:
            diff = next_num - num
            if diff in preamble:
                valid = True
                break
        if not valid:
            invalid_num = next_num
            break

        start += 1
        end += 1

    elapsed_time = (time.time() - start_time) * 1e3
    print(invalid_num, f"time elapsed: {elapsed_time} ms")
    start_time = time.time()
    start, end = find_contiguous_sum(input_, len(input_), invalid_num)
    range_ = input_[start:end]
    elapsed_time = (time.time() - start_time) * 1e3
    print(min(range_) + max(range_), f"time elapsed: {elapsed_time} ms")


def find_contiguous_sum(nums, n, sum_):
    curr_sum = nums[0]
    start = 0

    i = 1
    while i <= n:
        while curr_sum > sum_ and start < i - 1:
            curr_sum = curr_sum - nums[start]
            start += 1

        if curr_sum == sum_:
            return (start, i - 1)

        curr_sum = curr_sum + nums[i]
        i += 1

    return 0


def main():
    input_ = read_input()
    solve(input_)


if __name__ == "__main__":
    main()
