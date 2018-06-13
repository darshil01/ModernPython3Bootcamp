'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''
import csv

def update_users(o_first, o_last, n_first, n_last):
    with open("users.csv", "r", encoding="UTF-8") as f:
        csv_reader = csv.reader(f)
        rows = list(csv_reader)
    
    count = 0
    with open("users1.csv", 'w') as f:
        csv_writer = csv.writer(f)
        for row in rows:
            if row[0] == o_first and row[1] == o_last:
                csv_writer.writerow([n_first, n_last])
                count += 1
            else:
                csv_writer.writerow(row)
            
    return "Users updated: {}".format(count)

print(update_users("Grace", "Hopper", "Hello", "World"))
print(update_users("Colt", "Steele", "Boba", "Fett"))
print(update_users("Not", "Here", "Still not", "Here"))
