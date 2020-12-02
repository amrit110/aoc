"""Create skeleton solution script for given day."""


import argparse
import os
from os.path import join
from shutil import copyfile


def parse_args():
    parser = argparse.ArgumentParser(description='Bootstrap')
    parser.add_argument('-y', '--year', required=True, type=int, help='year')
    parser.add_argument('-d', '--day', required=True, type=int, help='day')

    return parser.parse_args()


def bootstrap_solution(year, day):
    target_dir = join(f'{year}', f'day{day}')
    os.makedirs(target_dir, exist_ok=True)
    skeleton_script_path = join(target_dir, 'solve.py')
    
    if not os.path.exists(skeleton_script_path):
        template_script_path = join('.', 'template.py')
        copyfile(template_script_path, skeleton_script_path)

        print(f'Created skeleton for year-{year}, day-{day}')

    # Create empty input text file
    input_file_path = join(target_dir, 'input.txt')
    if not os.path.exists(input_file_path):
        with open(input_file_path, 'w') as f:
            pass


def main():
    args = parse_args()
    day = args.day
    year = args.year
    bootstrap_solution(year, day)


if __name__ == '__main__':
    main()
