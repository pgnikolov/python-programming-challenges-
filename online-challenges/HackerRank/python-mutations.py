def mutate_string(string, position, character):
    slist = [char for char in string]
    slist.pop(position)
    slist.insert(position, character)
    return ''.join(slist)
