# Don't forget to import re!
import re
import pdb
# Define is_valid_time below:
def is_valid_time(time_str):
    time_regex = re.compile(r"^[0-9]?[0-9]:[0-9]{2}$")
    match = time_regex.search(time_str)
    pdb.set_trace()
    if match:
        return True
    return False

print(is_valid_time("10:45"))