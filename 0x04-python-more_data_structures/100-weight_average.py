#!/usr/bin/pyton3
def weight_average(my_list=[]):
    prod = 0
    total_w = 0
    for item in my_list:
        prod += item[0] * item[1]
        total_w += item[1]
    return prod / total_w
        
