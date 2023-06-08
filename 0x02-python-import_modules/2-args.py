#!/usr/bin/python3
import sys


def main():
    argv = sys.argv
    argsLen = len(argv)
    if argsLen > 1:
        if argsLen == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(argsLen - 1))
        for i in range(1, argsLen):
            print("{}: {}".format(i, argv[i]))
    else:
        print("0 arguments.")


if __name__ == "__main__":
    main()
