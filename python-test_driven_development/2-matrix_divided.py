#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix of integers or floats")
