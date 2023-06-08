#!/usr/bin/python3
import sys
from sys import argv
from calculator_1 import add, sub, mul, div


def main():
    arg_len = len(argv)
    if arg_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif arg_len == 4:
        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])
        if operator not in ["+", "-", "*", "/"]:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            if operator == '+':
                result = add(a, b)
            elif operator == '-':
                result = sub(a, b)
            elif operator == '*':
                result = mul(a, b)
            elif operator == '/':
                result = div(a, b)
            else:
                print("Unknown operator. Available operators: +, -, * and /")
                sys.exit(1)
            print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    main()
