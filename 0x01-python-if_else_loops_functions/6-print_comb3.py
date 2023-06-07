#!/usr/bin/python3
for i in range(0, 100, 10):
    for j in range(1, 10):
        if i + j == 89:
            print("{}".format(i + j))
        elif i+j > ((i // 10) * 11):
            print("{:02d}, ".format(i + j), end='')
