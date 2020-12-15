#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time
import math


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
    lines = list(line for line in input_)
    ts = int(lines[0])
    ids = lines[1].split(",")
    first_bus_id, time_to_first_bus = None, math.inf
    for id_ in ids:
        if id_ == "x":
            continue
        else:
            id_ = int(id_)
        next_bus_ts = ((ts // id_) + 1) * id_
        time_to_bus = next_bus_ts - ts
        if time_to_bus < time_to_first_bus:
            time_to_first_bus = time_to_bus
            first_bus_id = id_

    print(first_bus_id * time_to_first_bus)


def solve_part2(input_):
    lines = list(line for line in input_)
    ids = lines[1].split(",")
    first_bus_id = int(ids[0])
    i = 1
    skip = 1
    for offset, id_ in enumerate(ids[1:], 1):
        if id_ == "x":
            continue
        while True:
            ch = (i * first_bus_id + offset) / int(id_)
            if ch.is_integer() and ch > 0:
                break
            i += skip
        skip *= int(id_)

    print(i * first_bus_id)


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
