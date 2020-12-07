#!/usr/bin/env python3

from os.path import dirname, realpath, join
from collections import defaultdict
import re


def transform_input(input_):
    # custom transform for the day
    input_ = input_.splitlines()
    bags = defaultdict(list)

    for line in input_:
        line = ''.join(line.split())
        src_bag_color = line.split('contain')[0]
        src_bag_color = re.sub('bags', '', src_bag_color)
        dst_bags = line.split('contain')[1].split(',')
        dst_bags = [re.sub('bag*.*', '', d) for d in dst_bags]

        if dst_bags[0] == 'noother':
            dst_bags = []
        
        dst_bags = [(int(d[0]), d[1:]) for d in dst_bags]
        bags[src_bag_color] = dst_bags

    return bags


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, 'input.txt'), 'r') as f:
        input_ = f.read()
        
    input_ = transform_input(input_)

    return input_


def recursive_search_part1(bag_color, bags_map, bags):
    count = 0
    bag_colors = set([bag[1] for bag in bags])
    if ('shinygold' in bag_colors):
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
    count = recursive_search_part2(input_, 'shinygold')
    print(count)


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == '__main__':
    main()
