import re

def parse_bytes(str1):
    reg_str = re.compile(r'(\b[0-1]{8}\b)')
    match = reg_str.findall(str1)
    return match

print(parse_bytes("11010101 10110010 11111010 322"))

