#!/usr/bin/env python3

from os.path import dirname, realpath, join
import itertools
from collections import deque
import numpy as np


def transform_input(input_):
    # custom transform for the day
    input_ = input_.splitlines()

    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, 'input.txt'), 'r') as f:
        input_ = f.read()
        
    input_ = transform_input(input_)

    return input_


def find_row(row_code):
    range_ = list(range(128))
    for c in row_code:
        if c == 'F':
            start = 0
            end = int(len(range_) / 2)
        elif c == 'B':
            start = int(len(range_) / 2)
            end = int(len(range_))
            
        range_ = range_[start:end]

    return range_[0]


def find_col(col_code):
    range_ = list(range(8))
    for c in col_code:
        if c == 'L':
            start = 0
            end = int(len(range_) / 2)
        elif c == 'R':
            start = int(len(range_) / 2)
            end = int(len(range_))

        range_ = range_[start:end]

    return range_[0]


def gen_seat_ids(passes):
    seat_ids = []
   
    for pass_ in passes:
        row_code = pass_[0:7]
        col_code = pass_[7:]
        row = find_row(row_code)
        col = find_col(col_code)

        seat_ID = row * 8 + col
        seat_ids.append(seat_ID)

    return seat_ids


def solve_part1(input_):
    seat_ids = gen_seat_ids(input_)
    print(max(seat_ids))


def gen_all_passes():
    row_combinations = [''.join(x) for x in itertools.product('FB', repeat=7)]
    col_combinations = [''.join(x) for x in itertools.product('RL', repeat=3)]

    all_passes = []
    for rc in row_combinations:
        for cc in col_combinations:
            all_passes.append(rc + cc)

    return all_passes


def solve_part2(input_):
    all_passes = gen_all_passes()
    all_ids = []
    
    for pass_ in all_passes:
        row_code = pass_[0:7]
        col_code = pass_[7:]
        row = find_row(row_code)
        col = find_col(col_code)
        seat_ID = row * 8 + col
        all_ids.append(seat_ID)

    seat_ids = gen_seat_ids(input_)

    missing = []
    for id_ in all_ids:
        if id_ not in seat_ids:
            missing.append(id_)

    missing = sorted(missing)
    for i in range(len(missing) - 1):
        if (missing[i + 1] - missing[i]) > 1:
            print(missing[i + 1])
            break


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == '__main__':
    main()
