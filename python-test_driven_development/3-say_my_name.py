#!/usr/bin/python3
"""
this module contains a function that prints a name
"""
def say_my_name(first_name, last_name=""):
    """
    prints "My name is <first name> <last name>"
    args:first_name: The first name, must be a string
    last_name: The last name, must be a string (default is an empty string)
    raises:TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
