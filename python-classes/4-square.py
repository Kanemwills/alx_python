#!/usr/bin/python3
"""A module containing a square"""

class Square:
    """A square class"""


    def __init__(self, size=0):
        """ initialize square 
        Args:
            size (int): size of the square
        """

        self.size = size  # Use the setter method to validate size

    @property
    def size(self):
        """ Gets value of size
        Returns:
            size (init)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Change the value of size
        Args:
            value (int): new value o size
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

        return self.__size ** 2

    def my_print(self):
        """ Print a square"""

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
