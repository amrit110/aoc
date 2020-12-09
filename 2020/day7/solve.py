#!/usr/bin/env python3

from os.path import dirname, realpath, join
from collections import defaultdict
import re


def transform_input(input_):
    # custom transform for the day
    input_ = input_.splitlines()
    bags_map = defaultdict(list)

    for line in input_:
        line = "".join(line.split())
        bag, bags_in_bag = line.split("contain")
        bag = re.sub("bags", "", bag)
        bags_in_bag = bags_in_bag.split(",")
        bags_in_bag = [re.sub("bag*.*", "", b) for b in bags_in_bag]

        if bags_in_bag[0] == "noother":
            bags_in_bag = []

        bags_in_bag = [(int(b[0]), b[1:]) for b in bags_in_bag]
        bags_map[bag] = bags_in_bag

    return bags_map


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        input_ = f.read()

    input_ = transform_input(input_)

    return input_


def recursive_search_part1(bag_color, bags_map, bags):
    count = 0
    bag_colors = set([bag[1] for bag in bags])
    if "shinygold" in bag_colors:
        return 1
    else:
        for bag in bags:
            count_bag = recursive_search_part1(bag[1], bags_map, bags_map[bag[1]])
            if count_bag > 0:
                return 1

    return count


def recursive_search_part2(bags_map, target_bc):
    count = 0
    bags_inside = bags_map[target_bc]
    for bag in bags_inside:
        count += bag[0]
        count += recursive_search_part2(bags_map, bag[1]) * bag[0]

    return count


def solve_part1(input_):
    count = 0
    bag_colors = list(input_.keys())
    for bc in bag_colors:
        count += recursive_search_part1(bc, input_, input_[bc])

    print(count)


def solve_part2(input_):
    count = recursive_search_part2(input_, "shinygold")
    print(count)


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == "__main__":
    main()
