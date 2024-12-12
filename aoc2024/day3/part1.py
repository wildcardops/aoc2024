import re

import click

@click.command()
def part1():
    data = load_data()
    matches = get_matches(data)
    print(f"Total: {calculate_total(matches)}")

    

def load_data():
    with open('inputs/day3/input.txt') as f:
        return f.read().strip()

def get_matches(data):
    return re.findall(r"mul\((\d+),(\d+)\)", data)

def calculate_total(matches):
    return sum(int(a) * int(b) for a, b in matches)