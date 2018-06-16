'''
valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''

def valid_parentheses(str1):
    s = []
    balanced = True
    index = 0
    while index < len(str1) and balanced:
        if str1[index] == "(":
            s.append(str1[index])
        elif str1[index] == ")":
            if len(s) == 0:
                balanced = False
            else:
                s.pop()
        index += 1
    return balanced and len(s) == 0

print(valid_parentheses("()")) # True 
print(valid_parentheses(")(()))")) # False 
print(valid_parentheses("(")) # False 
print(valid_parentheses("(())((()())())")) # True 
print(valid_parentheses('))((')) # False
print(valid_parentheses('())(')) # False
print(valid_parentheses('()()()()())()(')) # False
