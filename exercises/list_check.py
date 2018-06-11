'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''

def list_check(lst1):
    return all([isinstance(x, list) for x in lst1])

print(list_check([[],[1],[2,3], (1,2)])) # False
print(list_check([1, True, [],[1],[2,3]])) # False
print(list_check([[],[1],[2,3]])) # True
