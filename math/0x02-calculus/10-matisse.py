#!/usr/bin/env python3
"""Task 10. Derive happiness in oneself from a good day's work"""


def poly_derivative(poly):
    """Polynomial derivative"""
    if isa_poly(poly):
        exponents = list(range(0, len(poly)+1))
        result = list(map(lambda x, y: x*y, poly, exponents))
        return result[1:] if len(poly) > 1 else [0]
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
