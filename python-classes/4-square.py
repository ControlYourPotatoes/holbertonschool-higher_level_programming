#!/usr/bin/python3
"""This module have a class that defines a square """


class Square:
    """Definition of square attribute"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """return the sqr size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the sqr size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = value

    def area(self):
        """return sqr area"""
        return self._Square__size ** 2
