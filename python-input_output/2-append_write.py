#!/usr/bin/python3
"""This module have a function named append_write"""


def write_file(filename="", text=""):
    """ Append string to end of file and return character count"""
    with open(filename, 'w') as fd:
        return fd.write(text)
