#!/usr/bin/python3
"""This module have a function named append_write"""


def append_file(filename="", text=""):
    """ Append string to end of file and return character count"""
    with open(filename, 'a') as fd:
        return fd.write(text)
