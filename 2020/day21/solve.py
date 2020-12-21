#!/usr/bin/env python3

from os.path import dirname, realpath, join
import time
import re
from collections import defaultdict


def transform_input(input_):
    input_ = input_.strip()
    # custom transform for the day
    ingredients, allergens = re.findall(r"(.+) \(contains (.+)\)", input_)[0]
    allergens = "".join(allergens.split()).split(",")
    ingredients = ingredients.split()

    return ingredients, allergens


def read_input():
    dir_path = dirname(realpath(__file__))
    with open(join(dir_path, "input.txt"), "r") as f:
        for line in f:
            yield transform_input(line)


def match(foods):
    allergen_to_ingredients = defaultdict(list)
    count = defaultdict(int)
    for ingredients, allergens in foods:
        for ingredient in ingredients:
            count[ingredient] += 1
        for allergen in allergens:
            allergen_to_ingredients[allergen].append(set(ingredients))
    ingredient_to_allergens = {}
    while True:
        for allergen, ingredients in allergen_to_ingredients.items():
            possible_ingredients = set.intersection(*ingredients)
            if len(possible_ingredients) == 1:
                ingredient = next(iter(possible_ingredients))
                ingredient_to_allergens[ingredient] = allergen
                for ingredient_sets in allergen_to_ingredients.values():
                    for ingredient_set in ingredient_sets:
                        ingredient_set -= {ingredient}
                break
        else:
            break

    return ingredient_to_allergens, count


def solve_part1(input_):
    ingredient_to_allergens, count = match(input_)
    print(sum(map(count.get, count.keys() - ingredient_to_allergens.keys())))


def solve_part2(input_):
    ingredient_to_allergens, count = match(input_)
    print(
        ",".join(
            sorted(ingredient_to_allergens, key=lambda x: ingredient_to_allergens[x])
        )
    )


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
