#!/usr/bin/python3
""" Define A Function That Write in A Text File """


def write_file(filename="", text=""):
    """
    Write a function that writes a string to a text
    file (UTF8) and returns the number of characters written:
    You must use the with statement
    You don't need to manage file permission exceptions.

    Args:
    filename
    text

    Return:
    number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as theFilename:
        contents = theFilename.write(text)
    return contents
