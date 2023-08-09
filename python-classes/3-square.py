#!/usr/bin/python3
"""A module containing a square
"""

class Sqaure: 
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Gets value of size
        Returns:
            size (int)
        """

        return self.__size
    
    @size.setter
    def size(self, value):
        """Change the value of size
        Args:
            value (int): new value of size
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates the area of a square
        Returns:
            area
        """

        return self.__size * self.__size    
        