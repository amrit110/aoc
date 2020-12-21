#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time
import networkx as nx
import numpy as np
from itertools import product
from math import prod


MONSTER = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """  # noqa: W291


def parse_input(input_):
    input_ = input_.strip()
    # custom transform for the day
    tile_blocks = input_.split("\n\n")
    tiles = {}
    for block in tile_blocks:
        block = block.splitlines()
        id_ = int(block[0][5:9])
        tiles[id_] = np.array([[c == "#" for c in line] for line in block[1:]])
    return tiles


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "test_input.txt"), "r") as f:
        return f.read()


def get_symmetries(tile):
    for _ in range(4):
        yield tile
        yield np.flipud(tile)
        tile = np.rot90(tile)


def get_match(tile1, tile2):
    for tile in get_symmetries(tile2):
        if (tile1[0] == tile[-1]).all():
            return (-1, 0), tile
        if (tile1[-1] == tile[0]).all():
            return (1, 0), tile
        if (tile1[:, -1] == tile[:, 0]).all():
            return (0, 1), tile
        if (tile1[:, 0] == tile[:, -1]).all():
            return (0, -1), tile


def create_graph(tiles):
    G = nx.Graph()
    for (i, tile1), (j, tile2) in product(tiles.items(), repeat=2):
        if i > j and get_match(tile1, tile2):
            G.add_edge(i, j)

    return G


def solve_part1(tiles):
    G = create_graph(tiles)
    print(prod(k for k, v in G.degree() if v == 2))


def solve_part2(tiles):
    pass
    # G = create_graph(tiles)
    # NOTE: Approach
    # 1. Start with random tile, at (0, 0) do DFS and link all tiles that match
    # chaining them and keeping track of their locations relative to the start (0, 0).
    # 2. Now we know the order and locations where each tile goes. Apply offset so
    # that bigger image locations start from (0, 0).
    # 3. Arrange the tiles on the bigger image.
    # 4. Take the monster's array as a windowed mask, search through the big image
    # and count matched patches, i.e. num of monsters.
    # 5. Obtain final count of non-monster # pixels


def main():
    start_time = time.time()
    tiles = parse_input(read_input())
    solve_part1(tiles)
    elapsed_time = (time.time() - start_time) * 1e3
    print(f"Time elapsed for part 1: {elapsed_time} ms")

    start_time = time.time()
    solve_part2(tiles)
    elapsed_time = (time.time() - start_time) * 1e3
    print(f"Time elapsed for part 2: {elapsed_time} ms")


if __name__ == "__main__":
    main()
