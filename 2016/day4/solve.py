#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time
from collections import defaultdict


def transform_input(input_):
    # custom transform for the day
    input_ = input_.split("-")
    name = input_[0:-1]
    id_, checksum = input_[-1].split("[")
    checksum = checksum.replace("]", "").strip()

    return name, int(id_), checksum


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def solve_part1(input_):
    sum_ids_real = 0
    for (name, id_, checksum) in input_:
        name = "".join(name)
        counts = defaultdict(int)
        for s in name:
            counts[s] += 1
        counts = sorted(counts.items(), key=lambda x: x[0])
        counts = sorted(counts, key=lambda x: x[1], reverse=True)

        cs = "".join([c[0] for c in counts])[0:5]
        if cs == checksum:
            sum_ids_real += id_

    print(sum_ids_real)


def solve_part2(input_):
    for (name, id_, checksum) in input_:
        name = list("".join(name))
        for i, _ in enumerate(name):
            name[i] = chr((((ord(name[i]) - 97) + id_) % 26) + 97)

        name = "".join(name)
        if "north" in name:
            print(name, id_)


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
