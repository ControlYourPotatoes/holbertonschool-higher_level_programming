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

        def area(self):
            """This method return the area of the square"""
            return self.__size ** 2
