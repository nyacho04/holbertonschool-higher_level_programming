#!/usr/bin/python3
"""module that defines a class MyList"""


class BaseGeometry:
    """returns true if the object is exactly an instance of the specified class"""

    def area(self):
        """returns true if the object is exactly an instance of the specified class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
