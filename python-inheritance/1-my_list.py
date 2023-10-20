#!/usr/bin/python3
"""
This module contains class
named MyList that inherit from list.
"""


class MyList(list):
    """Class MyList that inherits from list"""
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        sorted = []
        for i in self:
            sorted.append(i)
        sorted.sort()
        print(sorted)

