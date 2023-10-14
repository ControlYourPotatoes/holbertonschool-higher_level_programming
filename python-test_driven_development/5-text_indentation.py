#!/usr/bin/python3
"""This module print texts"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for char in text:
        new_text += char
        if char in [".", "?", ":"]:
            new_text += "\n\n"

    lines = [line.strip() for line in new_text.split("\n")]
    for line in lines:
        print(line)

