#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
# My code
last = int(repr(number)[-1])
if number >= 0:
    if last > 5:
        print("Last digit of", number, "is", last, "and is greater than 5")
    elif last == 0:
        print("Last digit of", number, "is", last, "and is 0")
    else:
        print("Last digit of", number, "is", last, "and is less than 6 and not 0")
elif number < 0:
    if last == 0:
        print("Last digit of", number, "is", last, "and is 0")
    else:
        print("Last digit of", number, "is:", "-", last, "and is less than 6 and not 0")



