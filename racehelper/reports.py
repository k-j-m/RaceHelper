"""
Module provides functionality relating to race reporting
"""

__author__ = 'kenny'

def make_tabular_report(races):
    lines = []

    headers = ['start_time', 'type', 'name', 'distance', 'location_name']
    lines.append('\t'.join(headers))
    for race in races:
        row = []
        for h in headers:
            row.append(str(getattr(race, h)))
        lines.append('\t'.join(row))

    return '\n'.join(lines)