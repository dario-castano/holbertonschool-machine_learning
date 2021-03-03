#!/usr/bin/env python3
"""Task 10. Derive happiness in oneself from a good day's work"""


def poly_derivative(poly):
    """Polynomial derivative"""
    if isa_poly(poly) and len(poly) > 1:
        exponents = list(range(0, len(poly)+1))
        result = list(map(lambda x, y: x*y, poly, exponents))
        return result[1:]
    else:
        return None


def isa_poly(poly):
    """Checks if is a polynomial"""
    if type(poly) is list and all(list(map(lambda x: isa_number(x), poly))):
        return True
    else:
        return False


def isa_number(n):
    """Checks if is a number"""
    if type(n) is int or type(n) is float:
        return True
    else:
        return False
