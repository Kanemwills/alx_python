#!/usr/bin/python3
"""Defines a class Square"""


class square:
 """A square class with a private object attribute.Check the type of the argument and raises an exception on error"""   

def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
