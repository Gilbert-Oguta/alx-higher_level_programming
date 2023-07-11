#!/usr/bin/python3
"""
Module 3-is_same_class

This module contains one function
"""


def is_kind_of_class(obj, a_class):
    """
    checks instance of a specified a_class

    Args:
    obj - object to look for
    a_class - specified class

    Returns:
    True if the object is an instance of,
    or if the object is an instance of a class
    that inherited from, the specified class ;
    otherwise False.
    """
    return isinstance(obj, a_class)
