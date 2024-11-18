#!/usr/bin/python3
"""
Creating a function that rotates a 2D matrix by 90 degree
"""


def rotate_2d_matrix(matrix):
    """Function that rotates 2D matrix by 90 degree

    Args:
        matrix (list of lists): 2D matrix that must be rotated by 90 degree
        in-place

    Return:
        Nothing
    """

    temp = []
    edited_mat = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix) - 1, -1, -1):
            temp.append(matrix[j][i])
        edited_mat.append(temp)
        temp = []

    for i in range(len(edited_mat)):
        matrix[i] = edited_mat[i]
