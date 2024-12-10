import click

@click.command()
def part1():
    reports = load_data()
    report_list = parse_reports(reports)
    print(f"Number of valid reports: {process_reports(report_list)}")



def load_data() -> list:
    with open('inputs/day2/input.txt') as f:
        data = f.read().splitlines()
    return data


def parse_reports(reports: list) -> list:
    parsed = []
    for report in reports:
        parsed.append([int(x) for x in report.split(" ")])
    return parsed


def check_report_is_increasing(report: list) -> bool:
    return sorted(report) == report


def check_report_has_decending(report: list) -> bool:
    return sorted(report, reverse=True) == report


def check_change_within_tolerance(report: list) -> bool:
    report_head = report[:-1]
    report_tail = report[1:]
    for head, tail in zip(report_head, report_tail):
        if abs(head - tail) > 3 or abs(head - tail) < 1:
            return False
    return True

def process_reports(reports: list) -> int:
    valid_reports = 0
    for report in reports:
        if (check_report_is_increasing(report) or check_report_has_decending(report)) and check_change_within_tolerance(report):
            valid_reports += 1
    return valid_reports
