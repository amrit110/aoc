from itertools import cycle


def read_input():
    with open("input.txt", "r") as f:
        inp = f.read().splitlines()
        inp = [int(i) for i in inp]

    return inp


def solve_part1():
    inp = read_input()
    s = 0
    for i in inp:
        s += i

    print(s)


def solve_part2():
    inp = read_input()
    s = 0

    seen_freq = set()
    seen_freq.add(s)

    for i in cycle(inp):
        s += i
        if s in seen_freq:
            print(s)
            return
        seen_freq.add(s)


if __name__ == "__main__":
    solve_part1()
    solve_part2()
