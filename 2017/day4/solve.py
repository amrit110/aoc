#!/usr/bin/env python3

from os.path import dirname, realpath, join


def transform_input(input_):
    # custom transform for the day
    input_ = input_.split()

    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def solve_part1(input_):
    num_valid = 0
    for passphrases in input_:
        if len(set(passphrases)) == len(passphrases):
            num_valid += 1

    print(num_valid)


def solve_part2(input_):
    num_valid = 0
    for passphrases in input_:
        passphrases = [''.join(sorted(passphrase)) for passphrase in passphrases] 
        if len(set(passphrases)) == len(passphrases):
            num_valid += 1

    print(num_valid)


def main():
    solve_part1(read_input())
    solve_part2(read_input())


if __name__ == "__main__":
    main()
