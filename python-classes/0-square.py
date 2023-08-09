#!/usr/bin/python3
"""Defines a class Square"""


"""An square class with a private object attribute"""
class Square:
    def __init__(self, size=0):
        self.__size = size
        
Square = __import__('0-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
       