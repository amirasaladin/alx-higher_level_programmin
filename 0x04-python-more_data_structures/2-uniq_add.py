#!/usr/bin/python3
def uniq_add(my_list=[]):
    res_set = set(my_list)
    res = 0
    for i in res_set:
        res += i
    return res
