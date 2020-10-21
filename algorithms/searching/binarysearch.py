from math import floor

def binary_search(value, list):
    '''
    Iterates through half of the given list in search of the given value. 
    Returns the index of the item if found, returns -1 otherwise. 

    :param value: Value being searched for. 
    :param list: List that is being traversed. 
    :return: Index of found value, or -1 if not found. 
    '''
    if value <= list[floor(len(list) / 2)]:
        for x in range(floor(len(list) / 2) + 1):
            if value == list[x]:
                return x
        return -1
    else:
        for x in range(list[floor(len(list) / 2)], len(list)):
            if(value == list[x]):
                return x
        return -1