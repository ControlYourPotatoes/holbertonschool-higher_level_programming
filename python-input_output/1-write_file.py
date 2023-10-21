#!/usr/bin/python3
"""This module has function named write_file"""


def write_file(filename="", text=""):
    """
    Function that write a
    string to a text file and
    return character count
    """
    with open(filename, 'w') as fd:
        return fd.write(text)
