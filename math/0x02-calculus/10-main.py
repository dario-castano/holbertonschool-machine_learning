#!/usr/bin/env python3

poly_derivative = __import__('10-matisse').poly_derivative

poly = [5, 3, 0, 1]
print(poly_derivative(poly))

poly2 = [5]
print(poly_derivative(poly2))


poly3 = []
print(poly_derivative(poly3))