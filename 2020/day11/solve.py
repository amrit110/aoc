#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time
from collections import defaultdict


# adjacent neighbour directions
dirs = {x + y * 1j for x in (-1, 0, 1) for y in (-1, 0, 1)} - {0}


def transform_input(input_):
    # custom transform for the day

    return input_.strip()


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def run_sim(seats, adj_lookup, th):
    while True:
        is_any_seat_updated = False
        updated_seats = {}
        for z, occ in seats.items():
            adjs = adj_lookup[z]
            if occ:
                updated_seats[z] = sum(seats[adj] for adj in adjs) < th
            else:
                updated_seats[z] = not any(seats[adj] for adj in adjs)
            if updated_seats[z] != seats[z]:
                is_any_seat_updated = True
        seats = updated_seats
        if not is_any_seat_updated:
            return sum(seats.values())


def solve_part1(seats, floor):
    adj_lookup = {z: [z + d for d in dirs if z + d in seats] for z in seats}
    print(run_sim(seats, adj_lookup, 4))


def solve_part2(seats, floor):
    adj_lookup = defaultdict(list)
    for z, occ in seats.items():
        for d in dirs:
            seat_loc = z
            while True:
                seat_loc += d
                if seat_loc not in floor:
                    if seat_loc in seats:
                        adj_lookup[z].append(seat_loc)
                    break

    print(run_sim(seats, adj_lookup, 5))


def main():
    seats = dict()
    floor = set()
    for row, line in enumerate(read_input()):
        for col, char in enumerate(line):
            z = row + col * 1j
            if char == "L":
                seats[z] = False
            else:
                floor.add(z)

    start_time = time.time()
    solve_part1(seats, floor)
    elapsed_time = (time.time() - start_time) * 1e3
    print(f"Time elapsed for part 1: {elapsed_time} ms")

    start_time = time.time()
    solve_part2(seats, floor)
    elapsed_time = (time.time() - start_time) * 1e3
    print(f"Time elapsed for part 2: {elapsed_time} ms")


if __name__ == "__main__":
    main()
