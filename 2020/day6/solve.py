#!/usr/bin/env python3

from os.path import dirname, realpath, join


def transform_input(input_):
    # custom transform for the day
    input_ = input_.splitlines()
    groups = []
    persons = []
    last_line = len(input_)
    for i, line in enumerate(input_):
        if line == "" or last_line == i + 1:
            groups.append(persons)
            persons = []
        else:
            num_ans = set(list(line))
            persons.append(num_ans)

    return groups


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        input_ = f.read()

    input_ = transform_input(input_)

    return input_


def solve_part1(input_):
    count = 0
    for gr in input_:
        resp = set()
        for pr in gr:
            for r in pr:
                resp.add(r)
        count += len(resp)

    print(count)


def solve_part2(input_):
    count = 0
    for gr in input_:
        count += len(set.intersection(*gr))

    print(count)


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == "__main__":
    main()
