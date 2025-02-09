#!/usr/bin/python3
"""module that defines a class MyList"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """class"""

    def __init__(self, width, height):
        """initializes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
