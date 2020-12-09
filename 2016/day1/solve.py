#!/usr/bin/env python3

from os.path import dirname, realpath, join


def transform_input(input_):
    # custom transform for the day
    instructions = "".join(input_.split()).split(",")

    return instructions


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        input_ = f.read()

    input_ = transform_input(input_)

    return input_


def solve_part1(input_):
    current_position = [0, 0]
    heading = "north"
    directions = ["north", "east", "south", "west"]

    for instruction in input_:
        blocks = int(instruction[1:])
        if instruction[0] == "L":
            heading = directions[(directions.index(heading) - 1) % 4]
        elif instruction[0] == "R":
            heading = directions[(directions.index(heading) + 1) % 4]

        if heading == "north":
            current_position[1] += blocks
        if heading == "south":
            current_position[1] -= blocks
        if heading == "west":
            current_position[0] -= blocks
        if heading == "east":
            current_position[0] += blocks

    print(sum(current_position))


def solve_part2(input_):
    current_position = [0, 0]
    heading = "north"
    directions = ["north", "east", "south", "west"]
    visited = set()
    visited.add(tuple(current_position))

    for instruction in input_:
        blocks = int(instruction[1:])
        if instruction[0] == "L":
            heading = directions[(directions.index(heading) - 1) % 4]
        elif instruction[0] == "R":
            heading = directions[(directions.index(heading) + 1) % 4]

        if heading == "north":
            visited_now = [
                (current_position[0], current_position[1] + i + 1)
                for i in range(blocks)
            ]
            current_position[1] += blocks
        if heading == "south":
            visited_now = [
                (current_position[0], current_position[1] - (i + 1))
                for i in range(blocks)
            ]
            current_position[1] -= blocks
        if heading == "west":
            visited_now = [
                (current_position[0] - (i + 1), current_position[1])
                for i in range(blocks)
            ]
            current_position[0] -= blocks
        if heading == "east":
            visited_now = [
                (current_position[0] + (i + 1), current_position[1])
                for i in range(blocks)
            ]
            current_position[0] += blocks

        for v in visited_now:
            if v in visited:
                print(sum(v))
                return
            else:
                visited.add(v)


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == "__main__":
    main()
