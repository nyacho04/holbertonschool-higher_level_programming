#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """shape"""

    @abstractmethod
    def area(self):
        """area"""
        pass

    @abstractmethod
    def perimeter(self):
        """perimeter"""
        pass

class Circle(Shape):
    """shape"""

    def __init__(self, radius):
        """radius"""
        self.__radius = radius

    def area(self):
        """circle"""
        return math.pi * self.__radius ** 2

    def perimeter(self):
        """perimeter"""
        return 2 * math.pi * self.__radius

class Rectangle(Shape):
    """SRectangle"""

    def __init__(self, width, height):
        """Iheight"""
        self.__width = width
        self.__height = height

    def area(self):
        """rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """rectangle"""
        return 2 * (self.__width + self.__height)

def shape_info(shape):
    """shape"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
