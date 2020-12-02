#!/usr/bin/env python3

from os.path import dirname, realpath, join


def transform_input(input_):
    # custom transform for the day
    input_ = input_.splitlines()
    input_pwds = []
    for line in input_:
        count, letter, pwd = line.replace(':', '').split()
        low, high = count.split('-')
        input_pwds.append((int(low), int(high), letter, pwd))

    return input_pwds


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, 'input.txt'), 'r') as f:
        input_ = f.read()
        
    input_ = transform_input(input_)

    return input_


def solve_part1(input_):
    num_valid = 0
    for input_pwd in input_:
        pwd = list(input_pwd[-1])
        letter_count = len([s for s in pwd if s == input_pwd[2]])
        if letter_count >= input_pwd[0] and letter_count <= input_pwd[1]:
            num_valid += 1

    print(num_valid)


def solve_part2(input_):
    num_valid = 0
    for input_pwd in input_:
        pwd = list(input_pwd[-1])
        if (pwd[input_pwd[0] - 1] == input_pwd[2]) and \
                (pwd[input_pwd[1] - 1] != input_pwd[2]):
            num_valid += 1
        elif (pwd[input_pwd[0] - 1] != input_pwd[2]) and \
                (pwd[input_pwd[1] - 1] == input_pwd[2]):
            num_valid += 1

    print(num_valid)


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == '__main__':
    main()
