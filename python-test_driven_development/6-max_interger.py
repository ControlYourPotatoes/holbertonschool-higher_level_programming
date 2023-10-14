#!/usr/bin/python3
"""Module to find the max integer in a list"""


def max_integer(list=[]):
    """function to find and return max integer in a list"""

    if not list:
        return None
    max_int = list[0]
    
    for i in range(1, len(list)):
        if list[i] > max_int:
            max_int = list[i]
    return max_int
