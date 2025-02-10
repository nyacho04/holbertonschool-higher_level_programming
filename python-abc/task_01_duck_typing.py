#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        if radius < 0:
            raise ValueError
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius

class Rectangle(Shape):

    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
