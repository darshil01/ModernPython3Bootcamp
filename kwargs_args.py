def combine_words(root, **kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + root
    elif 'suffix' in kwargs:
        return root + kwargs['suffix']
    else:
        return(root)