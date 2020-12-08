#!/usr/bin/env python3

from os.path import dirname, realpath, join


def transform_input(input_):
    # custom transform for the day
    input_ = input_.splitlines()
    instructions = []
    
    for line in input_:
        instruction, val = line.split()
        instructions.append((instruction, int(val)))

    return instructions


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, 'input.txt'), 'r') as f:
        input_ = f.read()
        
    input_ = transform_input(input_)

    return input_


def run_program(instructions, instruction_pointer, visited_instructions, acc_global):
    if instruction_pointer in visited_instructions:
        return 0, acc_global
    elif instruction_pointer == len(instructions):
        return 1, acc_global

    instruction, val = instructions[instruction_pointer]
    visited_instructions.add(instruction_pointer)
    if instruction == 'acc':
        acc_global += val
        instruction_pointer += 1
    elif instruction == 'jmp':
        instruction_pointer += val
    else:
        instruction_pointer += 1

    acc_global = run_program(instructions, 
                             instruction_pointer, 
                             visited_instructions,
                             acc_global)

    return acc_global


def solve_part1(input_):
    visited_instructions = set()
    acc_global = 0
    term, acc_global = run_program(input_, 0, visited_instructions, acc_global)
    print(acc_global)


def solve_part2(input_):
    jump_locs = [i for i, v in enumerate(input_) if v[0] == 'jmp']
    nop_locs = [i for i, v in enumerate(input_) if v[0] == 'nop']

    def run_modified_program(instructions):
        acc_global = 0
        visited_instructions = set()
        term, acc_global = run_program(mod_input, 0, 
                                       visited_instructions, acc_global)

        if term:
            print(acc_global)

    for loc in jump_locs:
        mod_input = input_.copy()
        old_instruction = mod_input[loc]
        mod_input[loc] = ('nop', old_instruction[1])
        run_modified_program(mod_input)

    for loc in nop_locs:
        mod_input = input_.copy()
        old_instruction = mod_input[loc]
        mod_input[loc] = ('jmp', old_instruction[1])
        run_modified_program(mod_input)


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == '__main__':
    main()
