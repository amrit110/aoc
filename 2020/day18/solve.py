#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time
import re


def transform_input(input_):
    input_ = input_.strip()
    # custom transform for the day
    input_ = "".join(input_.split())

    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


class fakeint(int):
    def __sub__(self, x):
        return fakeint(int(self) * x)

    def __add__(self, x):
        return fakeint(int(self) + x)

    def __and__(self, x):
        return fakeint(int(self) * x)


def parse_expr(expr: str, replace_op: str = "-"):
    expr = re.sub(r"(\d+)", r"fakeint(\1)", expr)
    expr = expr.replace("*", replace_op)
    return eval(expr)


def solve_part1(input_):
    s = sum(parse_expr(expr) for expr in input_)
    print(s)


def solve_part2(input_):
    s = sum(parse_expr(expr, "&") for expr in input_)
    print(s)


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
