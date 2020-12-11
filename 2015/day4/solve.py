#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time
import hashlib


def transform_input(input_):
    # custom transform for the day

    return input_.strip()


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def find_hash_key_prefix(secret_key, num_zeros):
    m = hashlib.md5
    num = 0
    while True:
        key = secret_key + f"{num}"
        md5_hash = m(key.encode("utf-8")).hexdigest()
        if md5_hash[0:num_zeros] == "0" * num_zeros:
            print(num)
            break
        num += 1


def solve_part1(input_):
    input_ = list(input_)[0]
    find_hash_key_prefix(input_, 5)


def solve_part2(input_):
    input_ = list(input_)[0]
    find_hash_key_prefix(input_, 6)


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
