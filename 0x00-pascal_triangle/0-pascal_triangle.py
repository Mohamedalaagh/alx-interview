#!/usr/bin/python3
"""
Module that returns pascal triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows for the Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
              Each inner list contains the values for each row.
    """
    triangle = []
    if n <= 0:
        return []
    for i in range(n):
        triangle.append([com(i, j) for j in range(i + 1)])
    return triangle


def factorial(n):
    """
    Computes the factorial of a given number.

    Args:
        n (int): The number for which the factorial is to be computed.

    Returns:
        int: The factorial of the input number.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def com(row, column):
    """
    Computes the binomial coefficient (combination)
    for the given row and column.

    Args:
        row (int): The row index (n) in the Pascal's triangle.
        column (int): The column index (k) in the Pascal's triangle.

    Returns:
        int: The value of the combination
        C(row, column) = row! / (column! * (row - column)!).
    """
    return factorial(row) // (factorial(column) * factorial(row - column))
