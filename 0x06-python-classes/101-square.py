#!/usr/bin/python3
"""
Square class definition
"""


class Square:
    """"
    Square class with private instance attribute size
    """
    def __init__(self, size=0, position=(0, 0)):
        """Args:
               size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
            self.position = position

    @property
    def size(self):
        """size: size of the square
        setter validating size is int and >= 0
        Raise:
             TypeError
             ValueError
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """size: size of the square
        setter validating size is int and >= 0
        Raise:
             TypeError and ValueError
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        position: gives position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        defines position setter values
        """
        if self._tuple_(value):
            self.__position = value
        elif not self._tuple_(value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def _tuple_(self, position):
        """
        check if it is a tuple and +ive integer
        """
        if type(position) is not tuple or len(position) != 2:
            return False
        elif type(position[0]) is not int or position[0] < 0:
            return False
        elif type(position[1]) is not int or position[1] < 0:
            return False
        else:
            return True

    def area(self):

