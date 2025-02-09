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

class Rectangle(BaseGeometry):
    """class"""

    def __init__(self, width, height):
        """initializes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
