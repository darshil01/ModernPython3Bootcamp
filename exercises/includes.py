'''
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''
import pdb

def includes(coll, val1, start=0):
    if type(coll) == dict:
        coll = [y for y in coll.values()]
    for x in range(start, len(coll)):
        if coll[x] == val1:
            return True
    return False


print(includes([1, 2, 3], 1, 2)) # False 
print(includes([1, 2, 3], 1)) # True 
print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes('abcd', 'b')) # True
print(includes('abcd', 'e')) # False
