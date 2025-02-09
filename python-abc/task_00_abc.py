#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """animal"""

    @abstractmethod
    def sound(self):
        """sound"""
        pass

class Dog(Animal):
    """inherate animal"""

    def sound(self):
        """dog"""
        return "Bark"

class Cat(Animal):
    """cat"""

    def sound(self):
        """cat"""
        return "Meow"