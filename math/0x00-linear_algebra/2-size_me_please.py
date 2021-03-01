#!/usr/bin/env python3
"""Task 2: Size me please"""


def matrix_shape(matrix):
    """Shape of a matrix"""
    return full_shape(matrix, [])


def full_shape(matrix, shape):
    """Shape of a matrix with an accumulator"""
    if type(matrix) is list:
        shape.append(len(matrix))
        return full_shape(matrix[0], shape)
    else:
        return shape

