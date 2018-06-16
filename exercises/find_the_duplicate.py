'''
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''
import pdb

def find_the_duplicate(lst1):
    lst1.sort()
    for x in range(len(lst1) - 1):
        if lst1[x] == lst1[x + 1]:
            return lst1[x]

print(find_the_duplicate([1,2,1,4,3,12])) # 1
print(find_the_duplicate([6,1,9,5,3,4,9])) # 9
print(find_the_duplicate([2,1,3,4])) # None


