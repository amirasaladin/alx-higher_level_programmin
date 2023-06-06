#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if(number > 0):
    ldigit = number % 10
else:
    ldigit = abs(number) % 10 * -1

p1 = f"Last digit of {number} is {ldigit} "
if (ldigit > 5):
    print(p1 + "and is greater than 5")
elif (ldigit == 0):
    print(p1 + "and is 0")
elif (ldigit < 6):
    print(p1 + "and is less than 6 and not 0")
