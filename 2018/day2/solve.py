

def read_input():
    with open("input.txt", "r") as f:
        inp = f.read().splitlines()

    return inp


def get_letter_counts(string):
    counts = dict()
    for s in string:
        if s not in counts:
            counts[s] = 1
        else:
            counts[s] += 1

    return counts


def solve_part1():
    inp = read_input()

    num_2s, num_3s = 0, 0
    for s in inp:
        counts = get_letter_counts(s)
        if 2 in counts.values():
            num_2s += 1
        if 3 in counts.values():
            num_3s += 1

    print(num_2s * num_3s)


def solve_part2():
    inp = read_input()

    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            num_diff = 0

            z = zip(inp[i], inp[j])

            for k, (a, b) in enumerate(z):
                if a != b:
                    num_diff += 1

            if num_diff == 1:
                print(inp[i][0:k] + inp[i][k + 1 :])
                return


if __name__ == "__main__":
    solve_part1()
    solve_part2()
