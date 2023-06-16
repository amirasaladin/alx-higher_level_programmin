#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_key = []
    for k, v in a_dictionary.items():
        if v == value:
            del_key.append(k)
    for key in del_key:
        del a_dictionary[key]
    return a_dictionary
