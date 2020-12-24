#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time
import re
from collections import Counter


directions = {"e": 2, "se": 1 - 1j, "sw": -1 - 1j, "w": -2, "nw": -1 + 1j, "ne": 1 + 1j}


def transform_input(input_):
    input_ = input_.strip()
    # custom transform for the day

    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def init_flip_tiles(input_):
    black_tiles = set()
    for line in input_:
        flip_tile = sum(directions[d] for d in re.findall("|".join(directions), line))
        if flip_tile in black_tiles:
            black_tiles.remove(flip_tile)
        else:
            black_tiles.add(flip_tile)
    return black_tiles


def solve_part1(input_):
    black_tiles = init_flip_tiles(input_)
    print(len(black_tiles))


def solve_part2(input_):
    black_tiles = init_flip_tiles(input_)
    for _ in range(100):
        updated_black_tiles = set()
        for direction in directions:
            neighbour_count = Counter(
                z + s for s in directions.values() for z in black_tiles
            )
            for loc, count in neighbour_count.items():
                if loc in black_tiles and 0 < count < 3:
                    updated_black_tiles.add(loc)
                elif loc not in black_tiles and count == 2:
                    updated_black_tiles.add(loc)
        black_tiles = updated_black_tiles
    print(len(black_tiles))


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
