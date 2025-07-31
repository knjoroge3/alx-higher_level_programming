#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []

    for row in matrix:
        squared_row = []
        for item in row:
            square = item ** 2
            squared_row.append(square)
        result.append(squared_row)

    return (result)
