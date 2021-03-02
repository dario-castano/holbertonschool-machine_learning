#!/usr/bin/env python3

mat_mul = __import__('8-ridin_bareback').mat_mul

mat1 = [[1, 2],
        [3, 4],
        [5, 6]]
mat2 = [[1, 2, 3, 4],
        [5, 6, 7, 8]]
mat3 = []
mat4 = [1]
mat5 = [[5]]
mat6 = [[6]]
mat7 = [1,2,3,4,5]
mat8 = ['a',3, [1,2,3]]
print(mat_mul(mat1, mat2))
print(mat_mul(mat3, mat4))
print(mat_mul(mat5, mat6))
print(mat_mul(mat7, mat8))
print(mat_mul(mat2, mat1))

