'''
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
'''
import pdb

def range_in_list(lst1, start=0, end_index=0):
    if (end_index == 0) or (end_index > (len(lst1))):
        end_index = len(lst1) - 1
    new_list = []
    for x in range(start, end_index + 1):
        new_list.append(lst1[x])
    return sum(new_list)
    

print(range_in_list([1,2,3,4],0,2)) #  6
print(range_in_list([1,2,3,4],0,3)) # 10
print(range_in_list([1,2,3,4],1)) #  9
print(range_in_list([1,2,3,4])) # 10
print(range_in_list([1,2,3,4],0,100)) # 10
print(range_in_list([],0,1)) # 0
