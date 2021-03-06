"""Create skeleton solution script for given day."""


import argparse
import os
from os.path import dirname, realpath, join
from shutil import copyfile
from aocd import get_data


def parse_args():
    parser = argparse.ArgumentParser(description="Bootstrap")
    parser.add_argument("-y", "--year", required=True, type=int, help="year")
    parser.add_argument("-d", "--day", required=True, type=int, help="day")
    parser.add_argument(
        "-cpp",
        "--cpp",
        action="store_true",
        help="Bootstrap C++ template solution",
    )

    return parser.parse_args()


def download_input(year, day, dst_input_path):
    try:
        data = get_data(year=year, day=day)
        print(f"Fetched input year-{year}, day-{day}")
    except Exception:
        print("Failed to fetch input, creating empty input file")
        data = ""

    with open(dst_input_path, "w") as f:
        f.write(data)


def bootstrap_solution(year, day, cpp):
    target_dir = join(f"{year}", f"day{day}")
    os.makedirs(target_dir, exist_ok=True)
    dst_py = join(target_dir, "solve.py")
    dst_cpp = join(target_dir, "solve.cpp")

    if not os.path.exists(dst_py):
        src_py = join(dirname(realpath(__file__)), "template.py")
        copyfile(src_py, dst_py)
        print(f"Created python skeleton for year-{year}, day-{day}")

    if not os.path.exists(dst_cpp) and cpp:
        src_cpp = join(dirname(realpath(__file__)), "template.cpp")
        copyfile(src_cpp, dst_cpp)
        print(f"Created c++ skeleton for year-{year}, day-{day}")

    dst_input_path = join(target_dir, "input.txt")
    if not os.path.exists(dst_input_path):
        download_input(year, day, dst_input_path)


def main():
    args = parse_args()
    day = args.day
    year = args.year
    cpp = args.cpp
    bootstrap_solution(year, day, cpp)


if __name__ == "__main__":
    main()
