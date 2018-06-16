'''
reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''

def reverse_vowels(str1):
    stack = []
    new_word = []
    for letter in str1:
        if letter in "AEIOUaeiou":
            stack.append(letter)
    for x in range(len(str1)):
        if str1[x] in "AEIOUaeiou":
            new_word.append(stack.pop(-1))
        else:
            new_word.append(str1[x])
    return "".join(new_word)

print(reverse_vowels("Reverse Vowels In A String"))