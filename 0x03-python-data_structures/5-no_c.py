#!/usr/bin/python3
def no_c(my_string):
    my_string = [c for c in my_string if c not in "cC"]
    return "".join(my_string)
