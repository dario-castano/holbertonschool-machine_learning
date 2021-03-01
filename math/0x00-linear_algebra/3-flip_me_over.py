#!/usr/bin/env python3
"""Task 3: Flip Me Over"""


def matrix_transpose(matrix):
    """Transpose a matrix"""
    nrows = len(matrix)
    ncols = len(matrix[0])

    answer = zero_matrix(ncols, nrows)

    for row in range(nrows):
        for col in range(ncols):
            answer[col][row] = matrix[row][col]

    return answer


def zero_matrix(rows, cols):
    """Matrix filled with zeros"""
    return [([0]*cols) for _ in range(rows)]

