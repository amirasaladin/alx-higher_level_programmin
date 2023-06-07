#!/usr/bin/python3
def print_last_digit(number):
    if(number > 0):
        ldigit = number % 10
    else:
        ldigit = abs(number) % 10 * -1
    print(ldigit, end='')
print_last_digit(-1024)
