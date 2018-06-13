'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johonson
'''
import csv


def add_user(first, last):
    with open("users.csv", "a") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([first, last])    

add_user("Dwayne", "Johnson")

