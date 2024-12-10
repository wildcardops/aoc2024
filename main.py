import click

from aoc2024.day1.part1 import part1 as day1_part1
from aoc2024.day1.part2 import part2 as day1_part2

from aoc2024.day2.part1 import part1 as day2_part1
from aoc2024.day2.part2 import part2 as day2_part2



@click.group()
def cli():
    pass

@click.group()
def day1():
    pass
cli.add_command(day1)
day1.add_command(day1_part1)
day1.add_command(day1_part2)

@click.group()
def day2():
    pass
cli.add_command(day2)
day2.add_command(day2_part1)
day2.add_command(day2_part2)



if __name__ == '__main__':
    cli()