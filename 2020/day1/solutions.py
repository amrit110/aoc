def read_input():
    with open("input.txt", "r") as f:
        input = f.read().splitlines()
        input = [int(i) for i in input]

    return input


def part1():
    inp = read_input()
    diff = dict()

    for i in inp:
        d = 2020 - i
        if i not in diff:
            diff[d] = i
        else:
            print(d * i)
            return


def part2():
    inp = read_input()
    t = 2020
    len_ = len(inp)

    for i in range(0, len_ - 1):
        s = set()
        curr_sum = t - inp[i]
        for j in range(i + 1, len_):
            if (curr_sum - inp[j]) in s:
                print(inp[i] * inp[j] * (curr_sum - inp[j]))
                return
            s.add(inp[j])


if __name__ == "__main__":
    part1()
    part2()
