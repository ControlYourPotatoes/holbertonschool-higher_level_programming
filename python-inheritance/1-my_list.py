#!/usr/bin/python3
"""This module contains class inherit from list."""


class MyList(list):
    """Class MyList that inherits from list"""
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        list_sorted = []
        for num in self:
            list_sorted.append(num)
        list_sorted.sort()
        print(list_sorted)
