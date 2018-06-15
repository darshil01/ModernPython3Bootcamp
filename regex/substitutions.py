import re

# reg_str = re.compile(r'(blue|red|white)')

# print(reg_str.sub('colour', 'blue socks and red shoes'))
# 'colour socks and colour shoes'

# print(reg_str.subn('colour', 'blue socks and red shoes'))
# ('colour socks and colour shoes', 2)

text_str = "Last night Mrs. Daisy and Mr. White murdered Mr. Chow"

# reg_str = re.compile(r'(Mrs?.) (\b[a-zA-Z]+)')
reg_str = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+', re.I)
# print(reg_str.search(text_str).group())
print(reg_str.sub('\g<1> \g<2>**** ', text_str))