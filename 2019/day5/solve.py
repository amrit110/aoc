import math


def read_input(input_file):
    with open(input_file, 'r') as f:
        return [int(i.strip()) for i in f.read().split(',')]


class Intcode:

    def __init__(self, program):
        self.program = program

    def run_op1(self, val1, val2):
        return val1 + val2

    def run_op2(self, val1, val2):
        return val1 * val2

    def parse_opcode(self, opcode):
        new_opcode = int(opcode[-2:])
        mode3 = int(opcode[0])
        mode2 = int(opcode[1])
        mode1 = int(opcode[2])

        return mode3, mode2, mode1, new_opcode

    def get_val(self, mode, x):
        if mode == 0:
            return self.program[x]
        elif mode == 1:
            return x

    def run(self, opcode_idx=0):
        opcode = '{:05}'.format(self.program[opcode_idx])
        mode3, mode2, mode1, opcode = self.parse_opcode(opcode)

        if opcode == 99:
            return

        elif opcode in [1, 2]:
            param1 = self.get_val(mode1, self.program[opcode_idx + 1])
            param2 = self.get_val(mode2, self.program[opcode_idx + 2])
            res_pos = self.program[opcode_idx + 3]

            if opcode == 1:
                self.program[res_pos] = self.run_op1(param1, param2)
            elif opcode == 2:
                self.program[res_pos] = self.run_op2(param1, param2)

            opcode_idx += 4

        elif opcode == 3:
            res_pos = self.program[opcode_idx + 1]
            user_input = input("Enter input: ")
            self.program[res_pos] = int(user_input)

            opcode_idx += 2


        elif opcode == 4:
            output = self.get_val(mode1, self.program[opcode_idx + 1])
            print("Output: ", output)

            opcode_idx += 2

        elif opcode == 5:
            param1 = self.get_val(mode1, self.program[opcode_idx + 1])
            param2 = self.get_val(mode2, self.program[opcode_idx + 2])
            if param1 != 0:
                opcode_idx = param2
            else:
                opcode_idx += 3

        elif opcode == 6:
            param1 = self.get_val(mode1, self.program[opcode_idx + 1])
            param2 = self.get_val(mode2, self.program[opcode_idx + 2])
            if param1 == 0:
                opcode_idx = param2
            else:
                opcode_idx += 3

        elif opcode == 7:
            param1 = self.get_val(mode1, self.program[opcode_idx + 1])
            param2 = self.get_val(mode2, self.program[opcode_idx + 2])
            res_pos = self.program[opcode_idx + 3]
            if param1 < param2:
                self.program[res_pos] = 1
            else:
                self.program[res_pos] = 0

            opcode_idx += 4

        elif opcode == 8:
            param1 = self.get_val(mode1, self.program[opcode_idx + 1])
            param2 = self.get_val(mode2, self.program[opcode_idx + 2])
            res_pos = self.program[opcode_idx + 3]
            if param1 == param2:
                self.program[res_pos] = 1
            else:
                self.program[res_pos] = 0

            opcode_idx += 4

        self.run(opcode_idx)

    def __call__(self):
        self.run()


def solve_part1():
    program = read_input('input.txt')
    Intcode(program)()


def solve_part2():
    program = read_input('input.txt')
    Intcode(program)()

if __name__ == '__main__':
    solve_part1()
    solve_part2()
