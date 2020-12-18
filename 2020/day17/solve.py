#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time
from itertools import product


directions = list(product((-1, 0, 1), repeat=4))
directions.remove((0, 0, 0, 0))


def transform_input(input_):
    input_ = input_.strip()
    # custom transform for the day

    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def extend_range(index, active):
    coords = [a[index] for a in active]
    return range(min(coords) - 1, max(coords) + 2)


def print_active_xy(active):
    x_coords, y_coords, _, _ = zip(*active)
    xy_coords = [(a[0], a[1]) for a in active]
    x_range = min(x_coords), max(x_coords) + 1
    y_range = min(y_coords), max(y_coords) + 1
    for x in range(*x_range):
        line = ""
        for y in range(*y_range):
            if (x, y) in xy_coords:
                line += "#"
            else:
                line += "."
        print(line)
    print("---------------")


def run_sim(active, dims=3):
    # print_active_xy(active)
    for _ in range(6):
        updated_active = set()
        update = product(
            extend_range(0, active),
            extend_range(1, active),
            extend_range(2, active),
            extend_range(3, active) if dims == 4 else [0],
        )
        for x, y, z, w in update:
            count = sum(
                (x + dx, y + dy, z + dz, w + dw) in active
                for dx, dy, dz, dw in directions
            )
            # print(f'DEBUG: x:{x}, y:{y}, z:{z}, count:{count}')
            if (
                (x, y, z, w) in active
                and count in (2, 3)
                or (x, y, z, w) not in active
                and count == 3
            ):
                updated_active.add((x, y, z, w))
        active = updated_active
        # print_active_xy(active)
    return active


def solve_part1(active):
    active_result = run_sim(active)
    count = 0
    for a in active_result:
        if a[2] == 0:
            count += 1
        else:
            count += 2
    print(count)


def solve_part2(active):
    active_result = run_sim(active, dims=4)
    count = 0
    for a in active_result:
        if a[2] == 0:
            count += 1
        else:
            count += 2
    print(count)


def main():
    active = {
        (x, y, 0, 0)
        for x, line in enumerate(read_input())
        for y, c in enumerate(line)
        if c == "#"
    }

    start_time = time.time()
    solve_part1(active)
    elapsed_time = (time.time() - start_time) * 1e3
    print(f"Time elapsed for part 1: {elapsed_time} ms")

    start_time = time.time()
    solve_part2(active)
    elapsed_time = (time.time() - start_time) * 1e3
    print(f"Time elapsed for part 2: {elapsed_time} ms")


if __name__ == "__main__":
    main()
