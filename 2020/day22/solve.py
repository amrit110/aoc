#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time
from collections import deque


def transform_input(input_):
    input_ = input_.strip()
    # custom transform for the day
    decks = input_.split("\n\n")
    decks = [list(map(int, deck.splitlines()[1:])) for deck in decks]

    return decks


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        return transform_input(f.read())


def play_combat(p1_deck, p2_deck, recursive=False):
    seen = set()
    while p1_deck and p2_deck:
        p1_p2_deck = (tuple(p1_deck), tuple(p2_deck))
        if p1_p2_deck in seen:
            return 1, p1_deck
        seen.add(p1_p2_deck)
        p1_card = p1_deck.popleft()
        p2_card = p2_deck.popleft()
        if recursive and len(p1_deck) >= p1_card and len(p2_deck) >= p2_card:
            winnum, _ = play_combat(
                deque(list(p1_deck)[:p1_card]),
                deque(list(p2_deck)[:p2_card]),
                recursive=recursive,
            )
            winner = p1_deck if winnum == 1 else p2_deck
        else:
            if p1_card > p2_card:
                winner = p1_deck
            elif p2_card > p1_card:
                winner = p2_deck
        winner.append(p1_card if winner is p1_deck else p2_card)
        winner.append(p1_card if winner is not p1_deck else p2_card)
    return 1 if winner is p1_deck else 2, winner


def solve_part1(input_):
    p1_deck, p2_deck = input_
    winnum, winner = play_combat(deque(p1_deck), deque(p2_deck))
    print(sum(i * v for i, v in enumerate(reversed(winner), 1)))


def solve_part2(input_):
    p1_deck, p2_deck = input_
    winnum, winner = play_combat(deque(p1_deck), deque(p2_deck), recursive=True)
    print(sum(i * v for i, v in enumerate(reversed(winner), 1)))


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
