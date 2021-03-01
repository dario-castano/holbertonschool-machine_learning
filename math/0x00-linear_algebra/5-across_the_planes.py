#!/usr/bin/env python3
"""Task 5. Across The Planes"""


def add_matrices2D(mat1, mat2):
    """Adds two 2D matrices"""
    return list(map(lambda x, y: add_arrays(x, y), mat1, mat2)) if shape(mat1) == shape(mat2) else None


def add_arrays(arr1, arr2):
    """Adds two lists"""
    return list(map(lambda x, y: x+y, arr1, arr2)) if len(arr1) == len(arr2) else None


def shape(matrix):
    """Checks the shape of a matrix"""
    nrows = len(matrix)
    ncols = len(matrix[0]) if all(list(map(lambda x: len(x) == len(matrix[0]), matrix))) else 0

    return (nrows, ncols) if nrows != 0 and ncols != 0 else None

