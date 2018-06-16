'''
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''

# def is_odd_string(str1):
#     counter = 0
#     for letter in str1:
#         counter += (ord(letter) - 96)
#     if counter % 2 == 0:
#         return False
#     return True

def is_odd_string(str1):
    counter = [(ord(letter) - 96) for letter in str1]
    if sum(counter) % 2 == 0:
        return False
    return True


print(is_odd_string('a')) # True
print(is_odd_string('aaaa')) # False
print(is_odd_string('amazing')) # True
print(is_odd_string('veryfun')) # True
print(is_odd_string('veryfunny')) # False
