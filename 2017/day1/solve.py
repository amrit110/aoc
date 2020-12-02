#!/usr/bin/env python3

from os.path import dirname, realpath, join


def transform_input(input_):
    # custom transform for the day
    input_ = [int(d) for d in list(input_)]
    
    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, 'input.txt'), 'r') as f:
        input_ = f.read()
        
    input_ = transform_input(input_)
 
    return input_


def solve_part1(input_):
    num_digits = len(input_)
    sum_ = 0
    for i, d in enumerate(input_):
        if d == input_[(i + 1) % num_digits]:
            sum_ += d

    print(sum_)


def solve_part2(input_):
    num_digits = len(input_)
    sum_ = 0
    for i, d in enumerate(input_):
        if d == input_[(i + int(num_digits / 2)) % num_digits]:
            sum_ += d

    print(sum_)


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == '__main__':
    main()
