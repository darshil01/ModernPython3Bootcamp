def list_manipulation(lst1, cmd, location, value=0):
    if cmd == "remove":
        if location == "beginning":
            return lst1.pop(0)
        return lst1.pop(-1)
    
    if cmd == "add":
        if location == "beggining":
            st1.insert(0, value)
        else:
            lst1.append(value)
        return lst1