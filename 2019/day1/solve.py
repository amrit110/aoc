import math


def read_input(input_file):
    with open(input_file, 'r') as f:
        return f.read().splitlines()


def solve_part1():
    masses = read_input('input.txt')
    s = 0
    for mass in masses:
        s += (math.floor(float(mass) / 3)) - 2

    return s


def solve_part2():
    def compute_fuel(mass):
        tf = 0
        f = math.floor(float(mass) / 3) - 2
        if f > 0:
            tf += f + compute_fuel(f)

        return tf

    masses = read_input('input.txt')
    s = 0
    for mass in masses:
        s += compute_fuel(mass)

    return s


if __name__ == '__main__':
    print(solve_part1())
    print(solve_part2())
