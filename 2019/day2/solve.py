def read_input(input_file):
    with open(input_file, "r") as f:
        return [int(i.strip()) for i in f.read().split(",")]


class Intcode:
    def __init__(self, program):
        self.program = program

    def run_op(self, val1, val2, opcode):
        if opcode == 1:
            return val1 + val2
        elif opcode == 2:
            return val1 * val2

    def run(self, opcode_idx=0):
        opcode = self.program[opcode_idx]
        if opcode == 99:
            return
        else:
            val1 = self.program[self.program[opcode_idx + 1]]
            val2 = self.program[self.program[opcode_idx + 2]]
            res_pos = self.program[opcode_idx + 3]

            self.program[res_pos] = self.run_op(val1, val2, opcode)

            opcode_idx += 4
            self.run(opcode_idx)

    def __call__(self):
        self.run()
        return self.program


def solve_part1():
    program = read_input("input.txt")
    program[1] = 12
    program[2] = 2
    print(Intcode(program)()[0])


def solve_part2():
    program = read_input("input.txt")
    for i in range(100):
        for j in range(100):
            program_input = program.copy()
            program_input[1] = i
            program_input[2] = j
            res = Intcode(program_input)()[0]
            if res == 19690720:
                print(100 * i + j)


if __name__ == "__main__":
    solve_part1()
    solve_part2()
