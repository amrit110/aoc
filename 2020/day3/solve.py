#!/usr/bin/env python3

from os.path import dirname, realpath, join
import numpy as np


def transform_input(input_):
    # custom transform for the day
    sz = 3000
    map_ = np.zeros((sz, sz))
    input_ = input_.splitlines()
    for i, line in enumerate(input_):
        line_ = ''
        while len(line_) <= sz:
            line_ += line
        line_ = line_[0:sz]
        for j, p in enumerate(line_):
            if p == '#':
                map_[i][j] = -1

    return map_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, 'input.txt'), 'r') as f:
        input_ = f.read()
        
    input_ = transform_input(input_)

    return input_


def solve_part1(input_):
    i = 0
    j = 0
    s = 0
    while (i < input_.shape[0] and j < input_.shape[1]):
        if input_[i][j] == -1:
            s += 1
        i += 1
        j += 3

    print(s)


def solve_part2(input_):
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    trees_encountered = []
    for i, j in slopes:
        ii, jj = 0, 0
        s = 0
        while (ii < input_.shape[0] and jj < input_.shape[1]):
            if input_[ii][jj] == -1:
                s += 1
            ii += i
            jj += j

        trees_encountered.append(s)
        
    p = 1
    for e in trees_encountered:
        p *= e
    print(p)


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == '__main__':
    main()
