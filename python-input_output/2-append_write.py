#!/usr/bin/python3
"""This module have a function named append_write"""


def append_write(filename="", text=""):
    """
    This function appends a string at the
    end of a text file and return character count
    """
    with open(filename, 'a') as fd:
        return fd.write(text)