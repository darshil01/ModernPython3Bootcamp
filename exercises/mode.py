'''
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''
from statistics import mode as mde
# define mode below:

def mode(lst1):
    return mde(lst1)

print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))