#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = [[x ** 2 for x in sublist] for sublist in matrix]
    return result
