'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

def sum_pairs(lst1, num):
    for x in range(len(lst1)):
        for y in range(len(lst1) - 1):
            if lst1[x] + lst1[y + 1] == num:
                return [lst1[x], lst1[y + 1]]
    return []

print(sum_pairs([4,2,10,5,1], 6)) # [4,2]

