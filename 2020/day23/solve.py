#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time


def transform_input(input_):
    input_ = input_.strip()
    # custom transform for the day

    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


class Node:
    def __init__(self, value):
        self.prev = self.next = None
        self.value = value


class DoublyLinkedListWithLookup:
    def __init__(self, values):
        self.lookup = {}
        head = prev = None
        for value in values:
            node = Node(value)
            if not head:
                head = node
            if prev:
                prev.next = node
                node.prev = prev
            self.lookup[value] = prev = node
        head.prev = prev
        prev.next = head

    def get_next_cups(self, curr_cup_node):
        return [
            curr_cup_node.next.value,
            curr_cup_node.next.next.value,
            curr_cup_node.next.next.next.value,
        ]

    def get(self, key):
        return self.lookup[key]

    def move(self, key, dst):
        cup, dst = self.lookup[key], self.lookup[dst]
        prev_next = dst.next
        cup.prev.next = cup.next
        cup.next.prev = cup.prev
        dst.next.prev = cup
        dst.next = cup
        cup.prev = dst
        cup.next = prev_next


def simulate(cups, iterations):
    circle = DoublyLinkedListWithLookup(cups)
    curr_cup = circle.get(cups[0])
    for _ in range(iterations):
        next_cups = circle.get_next_cups(curr_cup)
        dst_cup = len(cups) if curr_cup.value == 1 else curr_cup.value - 1
        while dst_cup in next_cups:
            dst_cup = len(cups) if dst_cup == 1 else dst_cup - 1
        while next_cups:
            circle.move(next_cups.pop(), dst_cup)
        curr_cup = curr_cup.next
    return circle.get(1)


def solve_part1(input_):
    cups = list(map(int, next(input_)))
    one = simulate(cups, 100)
    result = ""
    curr_cup = one.next
    while curr_cup != one:
        result += str(curr_cup.value)
        curr_cup = curr_cup.next
    print(result)


def solve_part2(input_):
    cups = list(map(int, next(input_)))
    one = simulate(cups + list(range(10, 10 ** 6 + 1)), 10 ** 7)
    print(one.next.value * one.next.next.value)


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
