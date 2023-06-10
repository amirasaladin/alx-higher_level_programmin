#!/usr/bin/python3
def no_c(my_string):
    if my_string is "":
        return ""
    my_string = [c for c in my_string]
    new_string = ""
    for c in my_string:
        if c == 'c' or c == 'C':
            my_string.remove(c)
    for c in my_string:
        new_string += c
    return new_string
