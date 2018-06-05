'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(lst1):
    return [ x for x in lst1 if x]

print(compact([0,1,2,"",[], False, {}, None, "All done"]))
