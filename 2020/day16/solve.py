#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time
from collections import defaultdict
import re
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching


def transform_input(input_):
    input_ = input_.strip()
    # custom transform for the day

    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def process_input(input_):
    lines = [line for line in input_]
    line_breaks = [idx for idx, line in enumerate(lines) if line == ""]
    ranges = [
        list(map(int, re.findall("\d+", line))) for line in lines[: line_breaks[0]]
    ]
    your_ticket = [int(v) for v in lines[line_breaks[1] - 1].split(",")]
    nearby_tickets = [
        list(map(int, line.split(","))) for line in lines[line_breaks[1] + 2 :]
    ]

    return your_ticket, nearby_tickets, ranges


def solve_part1(input_):
    your_ticket, nearby_tickets, ranges = process_input(input_)
    error_rate = 0
    full_range = set()
    for r1, r2, r3, r4 in ranges:
        for v in range(r1, r2 + 1):
            full_range.add(v)
        for v in range(r3, r4 + 1):
            full_range.add(v)

    error_rate = sum(v for t in nearby_tickets for v in t if v not in full_range)
    print(error_rate)


def solve_part2(input_):
    your_ticket, nearby_tickets, ranges = process_input(input_)
    full_range = set()
    for r1, r2, r3, r4 in ranges:
        for v in range(r1, r2 + 1):
            full_range.add(v)
        for v in range(r3, r4 + 1):
            full_range.add(v)

    valid_tickets = [t for t in nearby_tickets if all(v in full_range for v in t)]
    valids_r = [
        [
            all((r1 <= v[i] <= r2) or (r3 <= v[i] <= r4) for v in valid_tickets)
            for r1, r2, r3, r4 in ranges
        ]
        for i in range(20)
    ]
    perm = maximum_bipartite_matching(csr_matrix(valids_r))
    dep_field_vals = [your_ticket[idx] for idx in perm][:6]
    s = 1
    for v in dep_field_vals:
        s *= v
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
