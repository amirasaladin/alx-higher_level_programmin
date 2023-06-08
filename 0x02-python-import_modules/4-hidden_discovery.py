#!/usr/bin/python3
import hidden_4


def main():
    names = dir(hidden_4)
    names_len = len(names)
    for i in range(names_len):
        if names[i][0] and names[i][1] != '_':
            print("{}".format(names[i]))


if __name__ == "__main__":
    main()
