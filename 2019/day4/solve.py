

def has_two_adjacent(pw):
    pw = str(pw)
    num_adj = 0
    for i in range(len(pw) - 1):
        if pw[i] == pw[i+1]:
            num_adj += 1

    if num_adj > 0:
        return True
    else:
        return False


def has_two_adjacent_exclusive(pw):
    pw = str(pw)

    unique = set(pw)
    for u in unique:
        occ = [pos for pos, i in enumerate(pw) if i == u]
        if (len(occ) == 2) and (occ[0] + 1 == occ[1]):
            return True

    return False


def does_not_decr(pw):
    pw = str(pw)
    for i in range(len(pw) - 1):
        if int(pw[i + 1]) < int(pw[i]):
            return False

    return True


def solve_part1():
    num = 0
    for pw in range(123257, 647015):
        if has_two_adjacent(pw) and does_not_decr(pw):
            num += 1

    print(num)


def solve_part2():
    num = 0
    for pw in range(123257, 647015):
        if has_two_adjacent_exclusive(pw) and does_not_decr(pw):
            num += 1

    print(num)


if __name__ == '__main__':
    solve_part1()
    solve_part2()
