'''
print_users() # None
# prints to the console:
# Colt Steele
'''
import csv

def print_users():
    with open("users.csv", 'r') as f:
        csv_reader = csv.DictReader(f)
        for user in csv_reader:
            print("{} {}".format(user['First Name'], user['Last Name']))
print_users() 