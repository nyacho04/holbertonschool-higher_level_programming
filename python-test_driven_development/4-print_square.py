#!/usr/bin/python3
"""
this module contains the function print_square
"""
def print_square(size):
    """
    prints a square with the character #
    args:size (int): The size length of the square
    raises:TypeError: If size is not an integer
    ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
