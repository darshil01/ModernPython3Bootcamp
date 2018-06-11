'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''

def vowel_count(str1):
    vowels = "aeiou"
    results = {}
    for letter in str1.lower():
        if letter in vowels:
            if results.get(letter):
                results[letter] += 1
            else:
                results[letter] = 1
    return results

print(vowel_count('awesome')) # {'a': 1, 'e': 2, 'o': 1}
print(vowel_count('Elie')) # {'e': 2, 'i': 1}
print(vowel_count('Colt'))# {'o': 1}
