'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''

def titleize(str1):
    new_str = ""
    for x in range(len(str1)):
        if x == 0:
            new_str += str1[0].upper()
        elif str1[x - 1] == " ":
            new_str += str1[x].upper()
        else:
            new_str += str1[x]
    return new_str

    # a = str1.split(" ")
    # b = [x for x in a]
    # c = [letter for letter in b]
    # return # " ".join(b)

print(titleize('this is awesome')) # "This Is Awesome"
print(titleize('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"