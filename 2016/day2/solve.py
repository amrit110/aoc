#!/usr/bin/env python3

from os.path import dirname, realpath, join


def transform_input(input_):
    input_ = input_.splitlines()
    # custom transform for the day

    return input_


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, 'input.txt'), 'r') as f:
        input_ = f.read()
        
    input_ = transform_input(input_)

    return input_


def solve_part1(input_):
    keypad = dict()
    for i in range(3):
        for j in range(3):
            keypad[(i, j)] = 3 * i + j + 1

    curr_pos = [1, 1]
    code = ''
    
    for moves in input_:
        for move in moves:
            if move == 'U':
                curr_pos[0] = max(0, curr_pos[0] - 1)
            elif move == 'D':
                curr_pos[0] = min(2, curr_pos[0] + 1)
            elif move == 'L':
                curr_pos[1] = max(0, curr_pos[1] - 1)
            elif move == 'R':
                curr_pos[1] = min(2, curr_pos[1] + 1)
        code += str(keypad[tuple(curr_pos)])

    print(code)


def fill_pattern(keypad):
    keypad[(0, 2)] = 1
    keypad[(1, 1)] = 2
    keypad[(1, 2)] = 3
    keypad[(1, 3)] = 4
    keypad[(2, 0)] = 5
    keypad[(2, 1)] = 6
    keypad[(2, 2)] = 7
    keypad[(2, 3)] = 8
    keypad[(2, 4)] = 9
    keypad[(3, 1)] = 'A'
    keypad[(3, 2)] = 'B'
    keypad[(3, 3)] = 'C'
    keypad[(4, 2)] = 'D'

    return keypad


def solve_part2(input_):
    keypad = dict()
    for i in range(5):
        for j in range(5):
            keypad[(i, j)] = -1

    keypad = fill_pattern(keypad)

    curr_pos = [2, 0]
    code = ''
    
    for moves in input_:
        for move in moves:
            if move == 'U':
                next_pos = (max(curr_pos[0] - 1, 0), curr_pos[1])
            elif move == 'D':
                next_pos = (min(curr_pos[0] + 1, 4), curr_pos[1])
            elif move == 'L':
                next_pos = (curr_pos[0], max(curr_pos[1] - 1, 0))
            elif move == 'R':
                next_pos = (curr_pos[0], min(curr_pos[1] + 1, 4))
                
            if keypad[next_pos] != -1:
                curr_pos = next_pos
 
        code += str(keypad[tuple(curr_pos)])

    print(code)


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == '__main__':
    main()
