#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time


moves = {">": 1 + 0j, "<": -1 + 0j, "^": 0 + 1j, "v": 0 - 1j}


def transform_input(input_):
    # custom transform for the day

    return input_.strip()


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def solve_part1(input_):
    visited = set()
    curr_pos = 0 + 0j
    visited.add(curr_pos)
    num_visited = 1

    for line in input_:
        for dir_ in line:
            curr_pos += moves[dir_]
            if curr_pos not in visited:
                num_visited += 1
                visited.add(curr_pos)
    print(num_visited)


def solve_part2(input_):
    visited = set()
    curr_pos_s = 0 + 0j
    curr_pos_rs = 0 + 0j

    visited.add(curr_pos_s)
    num_visited = 1

    for line in input_:
        for i, dir_ in enumerate(line):
            if i % 2 == 0:
                curr_pos_s += moves[dir_]
                if curr_pos_s not in visited:
                    num_visited += 1
                    visited.add(curr_pos_s)
            else:
                curr_pos_rs += moves[dir_]
                if curr_pos_rs not in visited:
                    num_visited += 1
                    visited.add(curr_pos_rs)

    print(num_visited)


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
