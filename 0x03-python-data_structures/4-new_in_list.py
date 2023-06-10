#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_len = len(my_list)
    new_list = [0 for i in range(list_len)]
    for i in range(list_len):
        if i == idx:
            new_list[i] = element
        else:
            new_list[i] = my_list[i]
    return new_list
