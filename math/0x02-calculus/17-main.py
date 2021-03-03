#!/usr/bin/env python3

poly_integral = __import__('17-integrate').poly_integral

poly = [5, 3, 0, 1]
print(poly_integral(poly))

p2 = []
print(poly_integral(p2))

p3 = [0]
print(poly_integral(p3, C=7))