#!/usr/bin/env python3

cat_matrices2D = __import__('7-gettin_cozy').cat_matrices2D

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6]]
mat3 = [[7], [8]]
mat4 = cat_matrices2D(mat1, mat2)
mat5 = cat_matrices2D(mat1, mat3, axis=1)
mat6 = [[1]]
mat7 = [[2]]
mat8 = cat_matrices2D(mat6, mat7)
mat9 = cat_matrices2D(mat6, mat7, axis=1)
mat10 = [[-54, -87, 56, -92, 81], [54, 16, -72, 42, 901]]
mat11 = [[12, 63], [-10, 69]]
mat12 = cat_matrices2D(mat10, mat11, axis=1)
print(mat4)
print(mat5)
mat1[0] = [9, 10]
mat1[1].append(5)
print(mat1)
print(mat4)
print(mat5)
print(mat8)
print(mat9)
print(mat12)
