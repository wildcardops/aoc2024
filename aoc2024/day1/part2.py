import click

from .part1 import load_input, parse_input

@click.command()
def part2():
    data = load_input("inputs/day1/input.txt")
    left, right = parse_input(data)
    print(f"Total distance: {calculate_total_distance(left, right)}")   

def calulate_distance(left, right_list):
    return left * right_list.count(left)

def calculate_total_distance(left_list, right_list):
    return sum([calulate_distance(left, right_list) for left in left_list])
