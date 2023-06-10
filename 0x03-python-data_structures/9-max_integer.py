#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    biggest = float("-inf")
    for i in my_list:
        if i > biggest:
            biggest = i
    return biggest
