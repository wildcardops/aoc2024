import click

@click.command()
def part1():
    data = load_input("inputs/day1/input.txt")
    left, right = parse_input(data)
    print(f"Total distance: {get_total_distance(left, right)}")


def load_input(input_file):
    with open(input_file, 'r') as f:
        return f.read().splitlines()
    
def parse_input(data):
    left_list = []
    right_list = []
    for x in data:
        left, right = x.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))
    return sorted(left_list), sorted(right_list)

def distance(left, right):
    return abs(left - right)

def get_total_distance(left, right):
    return sum([distance(left[i], right[i]) for i in range(len(left))])
