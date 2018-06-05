'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''
def isEven(num):
    return num % 2 == 0
    
def partition(lst1, func):
    truthy_list = []
    falsey_list = []
    for num in lst1:
        if func(num) == True:
            truthy_list.append(num)
        else:
            falsey_list.append(num)
    return [truthy_list, falsey_list]

print(partition([1,2,3,4], isEven))
