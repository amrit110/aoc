#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time
import re
from itertools import product


def transform_input(line):
    # custom transform for the day
    whitespace = re.compile(r"\s+")
    line = re.sub(whitespace, "", line)
    left, right = re.split("=", line)
    if left == "mask":
        return right
    else:
        mem_addr = int(re.match(".*?\\[(.*)].*", left).group(1))
        val = int(right)
        return mem_addr, val

    return line


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def solve_part1(input_):
    memory = {}
    for i, ins in enumerate(input_):
        if isinstance(ins, str):
            mask_unchanged = int("".join("1" if bit == "X" else "0" for bit in ins), 2)
            mask_write = int("".join("1" if bit == "1" else "0" for bit in ins), 2)
        else:
            addr, val = ins
            memory[addr] = (val & mask_unchanged) | mask_write

    print(sum(memory.values()))


def gen_mask_combinations(mask):
    floating = [i for i, m in enumerate(mask) if m == "X"]
    for c in product(["0", "1"], repeat=len(floating)):
        new_mask = list(mask)
        for i, mask_idx in enumerate(floating):
            new_mask[mask_idx] = c[i]

        yield int("".join(new_mask), 2)


def solve_part2(input_):
    memory = {}
    for i, ins in enumerate(input_):
        if isinstance(ins, str):
            mask = ins
        else:
            addr, val = ins
            addr_bin = format(addr, "036b")
            bitmask_addr = "".join(
                m if m != "0" else addr_bin[i] for i, m in enumerate(mask)
            )
            write_addrs = gen_mask_combinations(bitmask_addr)
            for write_addr in write_addrs:
                memory[write_addr] = val

    print(sum(memory.values()))


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
