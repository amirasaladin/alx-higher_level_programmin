#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        # check if the value for the key is a list
        if isinstance(a_dictionary[key], list):
            # if the value is a list, append the new value to it
            a_dictionary[key].append(value)
        else:
            # if the value is not a list, create a list with the existing value and the new value
            a_dictionary[key] = [a_dictionary[key], value]
    return a_dictionary
