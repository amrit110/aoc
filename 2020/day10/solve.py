"""Day1 2020."""
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


def solve_part2(input_):
    jo = [0] + sorted(list([v for v in input_]))
    jo = jo + [max(jo) + 3]
    paths = defaultdict(int)
    paths[0] = 1
    for i in range(1, len(jo)):
        for j in range(i)[::-1]:
            if jo[i] - jo[j] > 3:
                break
            paths[i] += paths[j]

    print(paths[len(jo) - 1])


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
