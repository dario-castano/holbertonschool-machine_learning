#!/usr/bin/env python3
"""Task 17. Integrate"""


def poly_integral(poly, C=0):
    """Polynomial integral"""
    if isa_poly(poly) and isa_number(C):
        exponents = list(range(1, len(poly)+1))
        result = list(map(lambda x, y: trim_float(x/y), poly, exponents))
        return [C] + result if result != [0] else [C]
    else:
        return None


def isa_poly(poly):
    """Checks if is a polynomial"""
    if type(poly) is list and has_only_numbers(poly):
        return True if len(poly) >= 1 else False
    else:
        return False


def has_only_numbers(lst):
    """Check if list has only numbers"""
    return all(list(map(lambda x: isa_number(x), lst)))


def isa_number(n):
    """Checks if is a number"""
    if type(n) is int or type(n) is float:
        return True
    else:
        return False


def trim_float(n):
    """Converts .0 floats to ints"""
    if n == 0:
        return 0
    elif 1 > n > -1:
        return n
    else:
        return int(n) if n % int(n) == 0.0 else n
