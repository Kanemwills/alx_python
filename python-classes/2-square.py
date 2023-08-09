#!/usr/bin/python3
"""Defines a class Square"""


class squares:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

"""Returns the area of the square"""       

def area(self):
        return self.__size ** 2
