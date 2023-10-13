#!/usr/bin/python3
"""This module contains a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number
    """

    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    div1 = "div must be a number"
    div2 = "division by zero"

    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or len(matrix) is 0:
        raise TypeError(err1)
    for element in matrix:
        if not isinstance(element, list):
            raise TypeError(err1)
        if len(matrix[0]) is not len(element):
            raise TypeError(err2)
        for j in element:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(err1)

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(err2)

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError(div1)

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError(div2)

    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
