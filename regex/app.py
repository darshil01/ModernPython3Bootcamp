import re
import pdb

def extract_phone(phone_text):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(phone_text)
    if match:
        return match.group()
    return "No numbers found"

# print(extract_phone("My number is 111 123-1234"))
# print(extract_phone("my other number is 222 234-34451234"))


def extract_phone_all(phone_text):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.findall(phone_text)
    if match:
        return match
    return "No numbers found"

# print(extract_phone_all("Number 1 501 123-1233, Number 2 345 345-2345, Number 3 123 346-12345"))


def is_valid_phone(phone_input):
    phone_regex = re.compile(r'^\b\d{3} \d{3}-\d{4}\b$')
    match = phone_regex.search(phone_input)
    if match:
        return True
    return False

print(is_valid_phone("My number is 111 123-1234"))
print(is_valid_phone("111 123-1234"))

