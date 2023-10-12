#!/usr/bin/python3
"""This module have a class that defines a square """


class Square:
    """Definition of square attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square"""
        self.size = size
        try:
            self.position = position
        except TypeError as err:
            print(err)

    @property
    def position(self):
        """return current position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set current position"""
        if (len(value) < 2 or type(value[0]) is not int or
            type(value[1]) is not int or value[0] < 0 or
                value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    @property
    def size(self):
        """check size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets current square size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """return square area"""
        return self._Square__size ** 2

    def my_print(self):
        """print a # square """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("{}{}".format(" " * self.position[0], "#" * self.__size))
