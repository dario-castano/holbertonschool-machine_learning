#!/usr/bin/env python3
"""Task 9. Our life is the sum total of all the decisions we
make every day, and those decisions are determined by our priorities"""


def summation_i_squared(n):
    """Sum of squares"""
    if type(n) is int:
        return sum(list(map(lambda x: x * x, range(1, n+1))))
    else:
        return None
