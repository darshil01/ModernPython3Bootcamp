'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''
import csv

def delete_users(o_first, o_last):
    with open("users.csv", "r", encoding="UTF-8") as f:
        csv_reader = csv.reader(f)
        rows = list(csv_reader)
    
    count = 0
    with open("users2.csv", 'w') as f:
        csv_writer = csv.writer(f)
        for row in rows:
            if row[0] == o_first and row[1] == o_last:
                count += 1
            else:
                csv_writer.writerow(row)
            
    return "Users deleted: {}".format(count)

print(delete_users("Grace", "Hopper"))
print(delete_users("Colt", "Steele"))
print(delete_users("Not", "Here"))
