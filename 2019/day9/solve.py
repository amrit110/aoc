

def read_input(input_file):
    with open(input_file, "r") as f:
        return [int(i.strip()) for i in f.read().split(",")]


class Intcode:
    def __init__(self, program):
        self.memory = self.init_memory(program)
        self.instruction_pointer = 0
        self.relative_base = 0
        self.halted = False

    def init_memory(self, program):
        memory = [0] * 4096
        for i, p in enumerate(program):
            memory[i] = p

        return memory

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
            return self.memory[x]
        elif mode == 1:
            return x
        elif mode == 2:
            return self.memory[self.relative_base + x]

    def _get_write_pos(self, instruction_pointer, mode):
        return (
            self.memory[instruction_pointer]
            if mode == 0
            else self.relative_base + self.memory[instruction_pointer]
        )

    def run(self):  # noqa: C901
        opcode = "{:05}".format(self.memory[self.instruction_pointer])
        mode3, mode2, mode1, opcode = self.parse_opcode(opcode)

        if opcode == 99:
            self.halted = True
            return

        elif opcode in [1, 2]:
            param1 = self.get_val(mode1, self.memory[self.instruction_pointer + 1])
            param2 = self.get_val(mode2, self.memory[self.instruction_pointer + 2])
            res_pos = self._get_write_pos(self.instruction_pointer + 3, mode3)

            if opcode == 1:
                self.memory[res_pos] = self.run_op1(param1, param2)
            elif opcode == 2:
                self.memory[res_pos] = self.run_op2(param1, param2)

            self.instruction_pointer += 4

        elif opcode == 3:
            res_pos = self._get_write_pos(self.instruction_pointer + 1, mode1)
            user_input = input("Enter input: ")
            self.memory[res_pos] = int(user_input)

            self.instruction_pointer += 2

        elif opcode == 4:
            output = self.get_val(mode1, self.memory[self.instruction_pointer + 1])
            print("Output: ", output)

            self.instruction_pointer += 2

        elif opcode == 5:
            param1 = self.get_val(mode1, self.memory[self.instruction_pointer + 1])
            param2 = self.get_val(mode2, self.memory[self.instruction_pointer + 2])
            if param1 != 0:
                self.instruction_pointer = param2
            else:
                self.instruction_pointer += 3

        elif opcode == 6:
            param1 = self.get_val(mode1, self.memory[self.instruction_pointer + 1])
            param2 = self.get_val(mode2, self.memory[self.instruction_pointer + 2])
            if param1 == 0:
                self.instruction_pointer = param2
            else:
                self.instruction_pointer += 3

        elif opcode == 7:
            param1 = self.get_val(mode1, self.memory[self.instruction_pointer + 1])
            param2 = self.get_val(mode2, self.memory[self.instruction_pointer + 2])
            res_pos = self._get_write_pos(self.instruction_pointer + 3, mode3)
            if param1 < param2:
                self.memory[res_pos] = 1
            else:
                self.memory[res_pos] = 0

            self.instruction_pointer += 4

        elif opcode == 8:
            param1 = self.get_val(mode1, self.memory[self.instruction_pointer + 1])
            param2 = self.get_val(mode2, self.memory[self.instruction_pointer + 2])
            res_pos = self._get_write_pos(self.instruction_pointer + 3, mode3)
            if param1 == param2:
                self.memory[res_pos] = 1
            else:
                self.memory[res_pos] = 0

            self.instruction_pointer += 4

        elif opcode == 9:
            param = self.get_val(mode1, self.memory[self.instruction_pointer + 1])
            self.relative_base += param
            self.instruction_pointer += 2

    def __call__(self):
        while not self.halted:
            self.run()


def solve_part1():
    program = read_input("input.txt")
    Intcode(program)()


def solve_part2():
    program = read_input("input.txt")
    Intcode(program)()


if __name__ == "__main__":
    # solve_part1()
    solve_part2()
