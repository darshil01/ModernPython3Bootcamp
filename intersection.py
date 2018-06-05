def intersection(lst1, lst2):
    return [x for x in lst1 if x in lst2]

def intersection(lst1, lst2):
    return [x for x in set(lst1) & set(lst2)]