'''
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''

def three_odd_numbers(lst1):
    for x in range(len(lst1) - 3):
        total = lst1[x] + lst1[x + 1] + lst1[x + 2]
        if total % 2 != 0:
            return True
    return False


print(three_odd_numbers([1,2,3,4,5]))