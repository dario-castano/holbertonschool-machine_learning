#!/usr/bin/env python3
"""Task 7. Gettin’ Cozy"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Matrix concatenation"""
    m1 = [elem.copy() for elem in mat1]
    m2 = [elem.copy() for elem in mat2]
    if axis == 0:
        return m1 + m2 if columns_len(mat1) == len(mat2[0]) else None
    elif axis == 1:
        return list(map(lambda x, y: x+y, m1, m2)) \
            if columns_len(mat1) == len(mat2) else None
    else:
        return None


def columns_len(matrix):
    """Get the column length of the matrix"""
    return len(matrix[0]) \
        if all(list(map(lambda x: len(x) == len(matrix[0]), matrix))) else None
