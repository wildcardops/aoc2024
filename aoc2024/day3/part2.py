import pprint
import re

import click

from .part1 import load_data, get_matches, calculate_total

@click.command()
def part2():
    data = load_data()
    clean_data = preprocess_data(data)
    matches = get_matches(clean_data)
    print(f"Total: {calculate_total(matches)}")
    

def preprocess_data(data):
    to_dos = []
    blocks = data.split("do()")
    for block in blocks:
        to_dos.append(block.split("don't()")[0])
    return "".join(to_dos)
