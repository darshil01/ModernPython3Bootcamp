import re

def censor(str1):
    reg_str = re.compile(r'([Ff]rack?[a-z]+)')
    match = reg_str.sub("CENSORED", str1)
    return match

print(censor("Frack you"))