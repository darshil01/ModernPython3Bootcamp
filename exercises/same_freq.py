'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''
# import pdb

def same_frequency(num1, num2):
    str1 = sorted([x for x in str(num1)])
    str2 = sorted([x for x in str(num2)])

    if len(str1) == len(str1 and str2):
        return True
    return False


    # print(str1)
    # print(str2)
    # pdb.set_trace()
    # if len(str1) != len(str2):
    #     return False
    



print(same_frequency(551122,221515)) # True
print(same_frequency(321142,3212215)) # False
print(same_frequency(1212, 2211)) # True
