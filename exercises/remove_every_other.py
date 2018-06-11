'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''

def remove_every_other(lst1):
    newlist = []
    for x in range(0,len(lst1), 2):
        newlist.append(lst1[x])
    return newlist

print(remove_every_other([1,2,3,4,5]))