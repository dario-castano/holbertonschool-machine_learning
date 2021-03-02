#!/usr/bin/env python3
"""Task 8. Ridin’ Bareback"""


def mat_mul(mat1, mat2):
    """Matrix multiplication"""
    if compatible(mat1, mat2):
        nrows = shape(mat1)[0]
        ncols = shape(mat2)[1]
        ans = zeros(nrows, ncols)

        for i in range(nrows):
            for j in range(ncols):
                row_i = get_row(mat1, i)
                col_j = get_col(mat2, j)
                ans[i][j] = dot(row_i, col_j)
        return ans
    else:
        return None


def zeros(rows, cols):
    """Makes a zero matrix"""
    return [([0]*cols) for _ in range(rows)]


def shape(matrix):
    """Checks the shape of the matrices"""
    nrows = len(matrix)

    if all(list(map(lambda x: len(x) == len(matrix[0]), matrix))):
        ncols = len(matrix[0])
    else:
        ncols = 0

    return (nrows, ncols) if nrows != 0 and ncols != 0 else None


def compatible(mat1, mat2):
    """Checks if 2 matrices are compatible"""
    if isa_matrix(mat1) and isa_matrix(mat2):
        m1_cols = shape(mat1)[1]
        m2_rows = shape(mat2)[0]
        return True if m1_cols == m2_rows else False
    else:
        return False


def dot(a, b):
    """Performs a dot product between 2 lists"""
    both_numlist = isa_number_list(a) and isa_number_list(b)

    if len(a) == len(b) and both_numlist:
        return sum(list(map(lambda x, y: x * y, a, b)))
    else:
        return None


def isa_matrix(elem):
    """Checks if the elem is a matrix"""
    if not (type(elem) is list) or len(elem) < 1:
        return False
    elif not (all(list(map(lambda x: type(x) is list, elem)))):
        return False
    elif not (all(list(map(lambda x: isa_number_list(x), elem)))):
        return False
    else:
        return True


def isa_number_list(lst):
    """Checks if the list contains only numbers"""
    return all(list(map(lambda x: isa_number(x), lst)))


def isa_number(n):
    """Checks if the element is a int or float"""
    return type(n) is int or type(n) is float


def get_col(matrix, num):
    """Returns the column of a matrix as list"""
    return [matrix[i][num] for i in range(len(matrix))]


def get_row(matrix, num):
    """Returns the row of a matrix as a list"""
    return matrix[num]
