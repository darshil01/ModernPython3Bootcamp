'''
min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]
'''
# import pdb

def min_max_key_in_dictionary(dict1):
    return [min(dict1.keys()), max(dict1.keys())]


print(min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'})) # [1,10]
print(min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"})) # [1,4]