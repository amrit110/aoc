"""Plot times for solving tasks (private leaderboard)."""

import os
from os.path import dirname, realpath, join
import argparse
import requests
import json
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt


BOARD_SAVE_PATH = join(dirname(realpath(__file__)), 'board.json')
YEAR = 2020


def parse_args():
    parser = argparse.ArgumentParser(description='Plot private leaderboard times')
    parser.add_argument('-f', '--board_file', default=None, 
            help='path to saved stats.json file (private leaderboard)')
    parser.add_argument('-u', '--user_id', default=None, 
            help='aoc user id, to fetch private leaderboard')

    return parser.parse_args()


def fetch_latest_private_leaderboard(user_id):
    session_cookie = os.environ['AOC_SESSION']
    private_board_url = f'https://adventofcode.com/{YEAR}/leaderboard/private/view/{user_id}.json'
    auth = {
        'session': session_cookie
    }
    r = requests.get(private_board_url, cookies=auth)

    with open(BOARD_SAVE_PATH, 'w') as f:
        json.dump(r.json(), f, indent=4)

    if r.ok:
        print('Fetched latest private leaderboard stats')


def time_elapsed(ts):
    ds = datetime.utcfromtimestamp(int(ts))
    start = datetime(ds.year, ds.month, ds.day, 5, 0)
    
    return (ds.hour - start.hour) * 3600 + \
            (ds.minute - start.minute) * 60 + (ds.second - start.second)


def get_star_times_in_seconds_elapsed(member_times):
    times = defaultdict(list)
    
    for member_id, stats in member_times.items():
        name = stats.get('name')
        if name is None:
            name = member_id
        
        completion_times = stats.get('completion_day_level')
        num_days = len(completion_times)
        for day in range(num_days):
            star_times = completion_times[str(day + 1)]
            first_star_ts = time_elapsed(star_times.get('1').get('get_star_ts'))
            second_star_ts = time_elapsed(star_times.get('2').get('get_star_ts'))
            
            times[name].append([first_star_ts, second_star_ts - first_star_ts])

    return times


def plot_times(board_file_path): 
    with open(board_file_path, 'r') as f:
        board = json.load(f)

    all_star_times = get_star_times_in_seconds_elapsed(board.get('members'))

    fig, (ax1, ax2) = plt.subplots(2, 1)
    for name, star_times in all_star_times.items():
        days = [d + 1 for d in list(range(len(star_times)))]
        ax1.plot(days, [star_time[0] for star_time in star_times], '-*')
        ax2.plot(days, [star_time[1] for star_time in star_times], '-*')

    ax1.set_ylabel('time to solve task 1 (s)')
    ax2.set_ylabel('time to solve task 2 (s)')
    ax2.set_xlabel('day')

    ax1.legend(list(all_star_times.keys()))
    ax2.legend(list(all_star_times.keys()))
    plt.show()


def main():
    args = parse_args()
    board_file_path = args.board_file
    user_id = args.user_id
    if board_file_path is None or not os.path.isfile(board_file_path):
        fetch_latest_private_leaderboard(user_id)
        board_file_path = BOARD_SAVE_PATH
    plot_times(board_file_path)


if __name__ == '__main__':
    main()
