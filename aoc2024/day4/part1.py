from pprint import pprint

import click

@click.command()
def part1():
    input = load_input()
    padded_input = pad_input(input)
    windows = apply_kernel(padded_input, 7)
    x_windows = [window for window in windows if window[3][3] == 'X']
    print(f'Total matches: {total_matches_in_windows(x_windows)}')


def load_input():
    with open('inputs/day4/input.txt') as f:
        lines = f.readlines()
        return [list(line.strip()) for line in lines]


def pad_input(input):
    left_right_padded = [['Q', 'Q', 'Q'] + row + ['Q', 'Q', 'Q'] for row in input]
    top_bottom_padding = ['Q'] * len(left_right_padded[0])
    return [top_bottom_padding] * 3 + left_right_padded + [top_bottom_padding] * 3

def apply_kernel(matrix, kernel_size):
    rows, cols = len(matrix), len(matrix[0])
    kernel_windows = []
    kernel_height, kernel_width = kernel_size, kernel_size
    
    # Slide the kernel over the matrix
    for i in range(rows - kernel_height + 1):  # Iterate over rows
        for j in range(cols - kernel_width + 1):  # Iterate over columns
            # Extract the current kernel window from the matrix
            window = [row[j:j+kernel_width] for row in matrix[i:i+kernel_height]]
            kernel_windows.append(window)
    return kernel_windows


def check_horizontal_right(window):
    return [window[3][3], window[3][4], window[3][5], window[3][6]] == ['X', 'M', 'A', 'S']

def check_horizontal_left(window):
    return [window[3][3], window[3][2], window[3][1], window[3][0]] == ['X', 'M', 'A', 'S']

def check_vertical_down(window):
    return [window[3][3], window[4][3], window[5][3], window[6][3]] == ['X', 'M', 'A', 'S']

def check_vertical_up(window):
    return [window[3][3], window[2][3], window[1][3], window[0][3]] == ['X', 'M', 'A', 'S']

def check_diagonal_down_right(window):
    return [window[3][3], window[4][4], window[5][5], window[6][6]] == ['X', 'M', 'A', 'S']

def check_diagonal_down_left(window):
    return [window[3][3], window[4][2], window[5][1], window[6][0]] == ['X', 'M', 'A', 'S']

def check_diagonal_up_right(window):
    return [window[3][3], window[2][4], window[1][5], window[0][6]] == ['X', 'M', 'A', 'S']

def check_diagonal_up_left(window):
    return [window[3][3], window[2][2], window[1][1], window[0][0]] == ['X', 'M', 'A', 'S']

def count_matches_in_window(window):
    matches_in_window = 0
    if check_horizontal_right(window):
        matches_in_window += 1
    if check_horizontal_left(window):
        matches_in_window += 1
    if check_vertical_down(window):
        matches_in_window += 1
    if check_vertical_up(window):
        matches_in_window += 1
    if check_diagonal_down_right(window):
        matches_in_window += 1
    if check_diagonal_down_left(window):
        matches_in_window += 1
    if check_diagonal_up_right(window):
        matches_in_window += 1
    if check_diagonal_up_left(window):
        matches_in_window += 1
    return matches_in_window

def total_matches_in_windows(windows):
    return sum([count_matches_in_window(window) for window in windows])