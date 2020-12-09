from itertools import permutations


def read_input(input_file):
    with open(input_file, "r") as f:
        return [int(i.strip()) for i in f.read().split(",")]


class Intcode:
    def __init__(self, program, amp_phase):
        self.program = program
        self.amp_phase = amp_phase
        self.amp_input = None
        self.output = None
        self.amp_phase_set = False
        self.halted = False
        self.opcode_idx = 0

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

    def run(self):  # noqa: C901
        opcode = "{:05}".format(self.program[self.opcode_idx])
        # print('DEBUG ', opcode, self.program)
        mode3, mode2, mode1, opcode = self.parse_opcode(opcode)

        if opcode == 99:
            self.halted = True
            return self.output

        elif opcode in [1, 2]:
            param1 = self.get_val(mode1, self.program[self.opcode_idx + 1])
            param2 = self.get_val(mode2, self.program[self.opcode_idx + 2])
            res_pos = self.program[self.opcode_idx + 3]

            if opcode == 1:
                self.program[res_pos] = self.run_op1(param1, param2)
            elif opcode == 2:
                self.program[res_pos] = self.run_op2(param1, param2)

            self.opcode_idx += 4

        elif opcode == 3:
            res_pos = self.program[self.opcode_idx + 1]
            if not self.amp_phase_set:
                self.program[res_pos] = int(self.amp_phase)
                self.amp_phase_set = True
            else:
                self.program[res_pos] = int(self.amp_input)

            self.opcode_idx += 2

        elif opcode == 4:
            output = self.get_val(mode1, self.program[self.opcode_idx + 1])
            # print("Output: ", output)
            self.output = output

            self.opcode_idx += 2

            return

        elif opcode == 5:
            param1 = self.get_val(mode1, self.program[self.opcode_idx + 1])
            param2 = self.get_val(mode2, self.program[self.opcode_idx + 2])
            if param1 != 0:
                self.opcode_idx = param2
            else:
                self.opcode_idx += 3

        elif opcode == 6:
            param1 = self.get_val(mode1, self.program[self.opcode_idx + 1])
            param2 = self.get_val(mode2, self.program[self.opcode_idx + 2])
            if param1 == 0:
                self.opcode_idx = param2
            else:
                self.opcode_idx += 3

        elif opcode == 7:
            param1 = self.get_val(mode1, self.program[self.opcode_idx + 1])
            param2 = self.get_val(mode2, self.program[self.opcode_idx + 2])
            res_pos = self.program[self.opcode_idx + 3]
            if param1 < param2:
                self.program[res_pos] = 1
            else:
                self.program[res_pos] = 0

            self.opcode_idx += 4

        elif opcode == 8:
            param1 = self.get_val(mode1, self.program[self.opcode_idx + 1])
            param2 = self.get_val(mode2, self.program[self.opcode_idx + 2])
            res_pos = self.program[self.opcode_idx + 3]
            if param1 == param2:
                self.program[res_pos] = 1
            else:
                self.program[res_pos] = 0

            self.opcode_idx += 4

        self.run()

    def __call__(self, amp_input):
        if self.halted:
            return self.output
        else:
            self.amp_input = amp_input
            self.run()
            return self.output


def solve_part1():
    program_orig = read_input("input.txt")
    max_output_so_far = 0
    for phase_seq in permutations(range(5)):
        amp_input = 0
        for p in phase_seq:
            program = program_orig.copy()
            out = Intcode(program, p)(amp_input)
            amp_input = out

        if out > max_output_so_far:
            max_output_so_far = out

    return max_output_so_far


def solve_part2():
    program_orig = read_input("input.txt")
    max_output_so_far = 0

    for phase_seq in permutations(range(5, 10)):
        amp_input = 0
        amplifiers_iccs = []

        # Initialize.
        for p in phase_seq:
            amplifiers_iccs.append(Intcode(program_orig.copy(), p))

        idx = 0
        while True:
            in_amp_idx = idx % 5
            out = amplifiers_iccs[in_amp_idx](amp_input)
            amp_input = out
            idx += 1
            halted = [a.halted for a in amplifiers_iccs]

            if False not in halted:
                break

        if out > max_output_so_far:
            max_output_so_far = out

    return max_output_so_far


if __name__ == "__main__":
    print(solve_part1())
    print(solve_part2())
