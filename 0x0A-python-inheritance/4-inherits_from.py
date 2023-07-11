#!/usr/bin/python3
"""
Module 4-inherits_from

This module contains one function
"""


def inherits_from(obj, a_class):
    """
    Determines if obj is an instance of a class that
    inherited from a_class

    Args:
    obj - object to look for
    a_class - specified class

    Returns:
    True if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class ;
    otherwise False.
    """
    return isinstance(obj, a_class) and obj.__class__ != a_class
