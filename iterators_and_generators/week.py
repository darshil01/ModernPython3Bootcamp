import pdb

def week():
    week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for day in week_list:
        yield day

pdb.set_trace()