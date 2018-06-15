import re
import pdb

def parse_date(date_str):
    regex_str = re.compile(r'^(?P<day>[0-9]{2})[\.,:/](?P<month>[0-9]{2})[\.,:/](?P<year>[0-9]{4})$')
    match = regex_str.search(date_str)
    if match:
        return {
            'd': match['day'],
            'm': match['month'],
            'y': match['year']
        }
    return None

print(parse_date("01,22,9123"))