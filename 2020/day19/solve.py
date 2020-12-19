#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time
import re


def transform_input(input_):
    input_ = input_.strip()
    # custom transform for the day

    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def get_rules(input_):
    rules = {}
    for line in input_:
        if line == "":
            return rules
        match = re.search(
            r"^(\d+): (?:\"(\w)\"|(\d+(?: \d+)*(?: \| \d+(?: \d+)*)*))$", line
        )
        rule_num = int(match.group(1))
        if match.group(2):
            rules[rule_num] = match.group(2)
        else:
            rules[rule_num] = [
                list(map(int, re.findall(r"\d+", option)))
                for option in match.group(3).split("|")
            ]


def get_msgs(input_):
    return [line for line in input_]


def match_rules(rules, rule_nums, msg):
    if not rule_nums:
        return not msg
    rule_num, *rule_nums = rule_nums
    rule = rules[rule_num]
    if isinstance(rule, str):
        return msg.startswith(rule) and match_rules(rules, rule_nums, msg[len(rule) :])
    else:
        return any(match_rules(rules, option + rule_nums, msg) for option in rule)


def solve_part1(rules, msgs):
    s = sum(match_rules(rules, [0], msg) for msg in msgs)
    print(s)


def solve_part2(rules, msgs):
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    s = sum(match_rules(rules, [0], msg) for msg in msgs)
    print(s)


def main():
    input_ = read_input()
    rules = get_rules(input_)
    msgs = get_msgs(input_)

    start_time = time.time()
    solve_part1(rules, msgs)
    elapsed_time = (time.time() - start_time) * 1e3
    print(f"Time elapsed for part 1: {elapsed_time} ms")

    start_time = time.time()
    solve_part2(rules, msgs)
    elapsed_time = (time.time() - start_time) * 1e3
    print(f"Time elapsed for part 2: {elapsed_time} ms")


if __name__ == "__main__":
    main()
