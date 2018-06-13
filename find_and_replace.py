'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''
import pdb 

def find_and_replace(filename, org_name, new_name):
    with open(filename, 'r+', encoding="UTF-8") as f:
        data = f.read()
        data = data.replace("Alice", "Colt")
    with open("testing2.txt", "w") as f2:
        f2.write(data)

find_and_replace('story.txt', 'Alice', 'Colt') 