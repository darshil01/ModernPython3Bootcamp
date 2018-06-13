'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''
import csv
import pdb

def find_user(first_name, last_name):
    with open("users.csv", "r") as f:
        csv_reader = csv.reader(f)
        for index, line in enumerate(csv_reader):
            first_name_match = first_name == line[0]
            last_name_match = last_name == line[1]
            if first_name_match and last_name_match:
                return index
        return "{} {} not found.".format(first_name, last_name)
    # pdb.set_trace()
print(find_user("Colt", "Steele"))
print(find_user("Alan", "Turing")) # 3
print(find_user("Not", "Here"))