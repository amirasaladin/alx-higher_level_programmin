#!/usr/bin/python3
import sys


def main():
    argv = sys.argv
    args_len = len(argv)
    total = 0
    for i in range(1, args_len):
        total += int(argv[i])
    print("{}".format(total))


if __name__ == "__main__":
    main()
