#!/usr/bin/python3
"""
Module with Pascal_triangle method that creates a pascal triangle of size `n`
"""


def pascal_triangle(n):
    """
    Method used to create and return a pascal triangle of size `n`.

    Parameters:
    -----------
        n: int
            Required size of pascal triangle.
    Returns:
        List of zero or more lists each sublist is a row of the triangle.
    """
    triangle = []
    for row in range(n):
        triangle.append(
            [
                triangle[-1][column] + triangle[-1][column - 1]
                if row > column > 0 else 1
                for column in range(row + 1)
            ]
        )
    return triangle
