'''
@show_args 
def do_nothing(*args, **kwargs):
    pass
    
do_nothing(1, 2, 3,a="hi",b="bye")

# Should print (on two lines): 
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}
'''

from functools import wraps

def show_args(fn):
    def wrapper(*args, **kwargs):
        fn()
        print("Here are the args: {}".format(args))
        print("Here are the kwargs: {}".format(kwargs))
    return wrapper

@show_args 
def do_nothing(*args, **kwargs):
    pass
    
do_nothing(1, 2, 3,a="hi",b="bye")
