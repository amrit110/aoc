#!/usr/bin/env python3

from os.path import dirname, realpath, join
import numpy as np
from collections import defaultdict


def transform_input(input_):
    # custom transform for the day
    events = defaultdict(list)
    input_ = sorted(input_.splitlines())

    for line in input_:
        line = line.replace("[", "").replace("]", "")
        minute = line.split()[1].split(":")[1]
        if "Guard" in line:
            guard_id = int(line.split()[3].replace("#", ""))
        if "wakes" in line:
            events[guard_id].append(("w", minute))
        if "sleep" in line:
            events[guard_id].append(("s", minute))

    return events


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        input_ = f.read()

    input_ = transform_input(input_)

    return input_


def populate_sleep_log(input_):
    sleep_log = np.zeros((len(input_), 60))
    index = 0

    for guard_id, g_events in input_.items():
        for g_event in g_events:
            if g_event[0] == "s":
                start = int(g_event[1])
            if g_event[0] == "w":
                stop = int(g_event[1])
                sleep_log[index][start:stop] += 1
        index += 1

    return sleep_log


def solve_part1(input_):
    guards = list(input_.keys())
    sleep_log = populate_sleep_log(input_)

    minutes_asleep = list(sleep_log.sum(1))
    max_asleep_index = minutes_asleep.index(max(minutes_asleep))
    gid_max_asleep = guards[max_asleep_index]
    g_sleep_log = list(sleep_log[max_asleep_index])
    g_max_sleep_minute = g_sleep_log.index(max(g_sleep_log))

    print(g_max_sleep_minute * gid_max_asleep)


def solve_part2(input_):
    guards = list(input_.keys())
    sleep_log = populate_sleep_log(input_)

    max_minute_guard = np.unravel_index(np.argmax(sleep_log), sleep_log.shape)
    max_minute_guard_id = guards[max_minute_guard[0]]
    max_minute = max_minute_guard[1]
    print(max_minute * max_minute_guard_id)


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == "__main__":
    main()
