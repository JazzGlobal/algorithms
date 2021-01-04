def linear_search(value, list):
    '''
    Iterates through the entirety of the given list in search of the given value.
    Returns the index of the item if found, returns -1 otherwise.
    
    :param value: Value being searched for.
    :param list: List that is being traversed.
    :return: Index of found value, or -1 if not found. 
    '''
    for x in list:
        if(value == list[x-1]):
            return x - 1
    return -1

# String based Linary Search 
#
# search_value = 'hello'
# sorted_values = ['a','abc','string', 'xeno','zebra','hello']
# print(linear_search(search_value, sorted_values))