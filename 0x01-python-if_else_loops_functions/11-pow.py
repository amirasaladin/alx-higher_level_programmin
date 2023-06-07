#!/usr/bin/python3
def pow(a, b):
    a1 = 1
    if (b > 0):
        for i in range(b):
            a1 *= a
    else:
        for i in range(abs(b)):
            a1 /= a
    return a1
