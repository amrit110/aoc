#!/usr/bin/env python3

from os.path import dirname, realpath, join


# constants
VALID_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
NUMERIC = [str(i) for i in list(range(10))]
VALID_HC = NUMERIC + ['a', 'b', 'c', 'd', 'e', 'f']
VALID_EC = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def transform_input(input_):
    # custom transform for the day
    input_ = input_.splitlines()
    passports = []
    passport = dict()

    for i, line in enumerate(input_):
        fields = line.split()
        for field in fields:
            k, v = field.split(':')
            passport[k] = v
        
        if fields == [] or i + 1 == len(input_):
            passports.append(passport)
            passport = dict()

    return passports


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, 'input.txt'), 'r') as f:
        input_ = f.read()
        
    input_ = transform_input(input_)

    return input_


def solve_part1(input_):
    num_valid = 0
    for i, passport in enumerate(input_):
        keys = passport.keys()
        is_valid = set(keys) & set(VALID_KEYS)
        if len(is_valid) == 8:
            num_valid += 1
        elif (len(is_valid) == 7) and ('cid' not in is_valid):
            num_valid += 1

    print(num_valid)


def validate_fields(passport):
    birth_yr = int(passport['byr'])
    issue_yr = int(passport['iyr'])
    exp_yr = int(passport['eyr'])
    height = passport['hgt']
    hair_color = passport['hcl']
    eye_color = passport['ecl']
    passport_id = passport['pid']

    if not 1920 <= birth_yr <= 2002:
        return False
    if not 2010 <= issue_yr <= 2020:
        return False
    if not 2020 <= exp_yr <= 2030:
        return False

    if (not 'cm' in height) and (not 'in' in height):
        return False
    if 'in' in height:
        h = height.replace('in', '')
        if not 59 <= int(h) <= 76:
            return False
    if 'cm' in height:
        h = height.replace('cm', '')
        if not 150 <= int(h) <= 193:
            return False
    
    if '#' not in hair_color:
        return False
    hc = hair_color.replace('#', '')
    if len(hc) != 6:
        return False
    for hc_i in hc:
        if hc_i not in VALID_HC:
            return False
    
    if eye_color not in VALID_EC:
        return False

    if len(passport_id) != 9:
        return False

    for n in passport_id:
        if n not in NUMERIC:
            return False

    return True


def solve_part2(input_):
    num_valid = 0
    VALID_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    for i, passport in enumerate(input_):
        keys = passport.keys()
        is_valid = set(keys) & set(VALID_KEYS)
        if len(is_valid) == 8 and validate_fields(passport):
            num_valid += 1
        elif (len(is_valid) == 7) and ('cid' not in is_valid) and \
                validate_fields(passport):
            num_valid += 1

    print(num_valid)


def main():
    input_ = read_input()
    solve_part1(input_)
    solve_part2(input_)


if __name__ == '__main__':
    main()
