#!/usr/bin/python3
"""module that defines a class MyList"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """rectangle"""

    def __init__(self, size):
        """initializes size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """square"""
        return self.__size * self.__size

    def __str__(self):
        """return the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
