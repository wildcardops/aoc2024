import click

from .part1 import load_data, parse_reports, check_change_within_tolerance, check_report_has_decending, check_report_is_increasing

@click.command()
def part2():
    reports = load_data()
    report_list = parse_reports(reports)
    print(f"Number of valid reports: {process_reports(report_list)}")


def process_reports(reports):
    valid_reports = 0
    for report in reports:
        for subreport in create_skip_index_reports(report):
            if (check_report_is_increasing(subreport) or check_report_has_decending(subreport)) and check_change_within_tolerance(subreport):
                valid_reports += 1
                break
    return valid_reports


def create_skip_index_reports(report: list) -> list[list[int]]:
    skip_index_reports = []
    for i in range(len(report)):
        skip_index_reports.append(report[:i] + report[i+1:])
    return skip_index_reports
