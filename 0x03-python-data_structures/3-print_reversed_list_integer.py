#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None or len(my_list) == 0:
        return
    for i in reversed(my_list):
        print("{:d}".format(i))
