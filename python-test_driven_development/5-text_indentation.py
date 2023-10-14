#!/usr/bin/python3
"""This module print texts"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for let in range(len(text)):
        if text[let] == '.' or text[let] == '?' or text[let] == ':':
            print(text[let])
            print()
        elif text[let] == " " and text[let - 1] in ['.', '?', ':']:
            continue
        else:
            print(text[let], end="")
