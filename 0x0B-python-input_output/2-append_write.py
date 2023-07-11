#!/usr/bin/python3
""" A function Appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends text to filename

    Args:
        - filename: name of the file
        - text: text to append
    Returns: number of characters added
    """
    with open(filename, mode="a", encoding='utf-8') as theFilename:
        contents = theFilename.write(text)
    return contents
