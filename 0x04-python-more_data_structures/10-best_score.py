#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    big_int = 0
    key = ""
    for k, v in a_dictionary.items():
        if v > big_int:
            big_int = v
            key = k
    return key
