'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(lst1):
    total = 1
    for x in lst1:
        if x % 2 == 0:
            total *= x
    return total

print(multiply_even_numbers([2,3,4,5,6]))
