#!/usr/bin/python3
"""This function will print My name is <first name> <last name>"""


def print_square(size):
    """
    Prints a square with the character #.
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for _ in range(size):
        print("#" * size)
