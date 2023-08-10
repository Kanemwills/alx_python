#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_row = [num ** 2 for num in row]
        squared_matrix.append(squared_row)
    return squared_matrix


