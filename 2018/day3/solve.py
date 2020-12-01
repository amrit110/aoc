
import numpy as np


def read_input():
    with open('input.txt', 'r') as f:
        inp = f.read().splitlines()

        claims = []
        for line in inp:
            x_min, y_min = line.split('@')[1].split(':')[0].split(',')
            w, h = line.split('@')[1].split(':')[1].split('x')
            rect = (int(x_min), int(y_min), int(x_min) + int(w), int(y_min) + int(h))
            claims.append(rect)

    return claims


def solve_part1():
    claims = read_input()
    fabric = np.zeros((1000, 1000))
    for claim in claims:
        fabric[claim[0]:claim[2], claim[1]:claim[3]] += 1

    two_or_more = fabric > 1
    print(two_or_more.sum())


def solve_part2():
    claims = read_input()
    fabric = np.zeros((1000, 1000))
    for claim in claims:
        fabric[claim[0]:claim[2], claim[1]:claim[3]] += 1

    for id_, claim in enumerate(claims):
        w, h = claim[2] - claim[0], claim[3] - claim[1]
        if fabric[claim[0]:claim[2], claim[1]:claim[3]].sum() == w * h:
            print(id_ + 1)


if __name__ == '__main__':
    solve_part1()
    solve_part2()
