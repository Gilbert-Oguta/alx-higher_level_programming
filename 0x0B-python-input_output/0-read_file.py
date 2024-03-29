#!/usr/bin/python3
"""
This is module 0-read_file

This module contains one function `read_file()`
"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8) and prints it to stdout
    You must use the with statement
    Args:
    filename
    """
    with open(filename, mode = "r", encoding='utf-8') as m_file:
        print(m_file.read(), end="")
