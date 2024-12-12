from pprint import pprint

import click

from .part1 import load_input, apply_kernel

@click.command()
def part2():
    input = load_input()
    windows = apply_kernel(input, 3)
    a_windows = filter_for_a_windows(windows)
    print(f'Total matches: {total_matches_in_windows(a_windows)}')

def filter_for_a_windows(windows):
    return [window for window in windows if window[1][1] == 'A']

def check_right_diagonal(window):
    return window[0][0] == 'M' and window[2][2] == 'S' or window[0][0] == 'S' and window[2][2] == 'M'

def check_left_diagonal(window):
    return window[0][2] == 'M' and window[2][0] == 'S' or window[0][2] == 'S' and window[2][0] == 'M'

def check_xmas(window):
    return check_right_diagonal(window) and check_left_diagonal(window)

def total_matches_in_windows(windows):
    return sum([check_xmas(window) for window in windows])
