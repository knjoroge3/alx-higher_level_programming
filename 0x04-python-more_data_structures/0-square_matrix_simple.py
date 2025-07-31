#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []

    for row in matrix:
        for item in row:
            square = item ** 2
            result.append(square)

    return (result)
