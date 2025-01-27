#!/usr/bin/python3
"""
this module contains the matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix by a given number
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix of integers or floats")
