#!/usr/bin/python3
"""module that defines a class MyList"""


def inherits_from(obj, a_class):
    """returns true if the object is exactly an instance of the specified class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
