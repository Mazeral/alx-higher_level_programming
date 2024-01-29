#!/usr/bin/python3
def matrix_divided(matrix, div):
    """matrix_divided A function which
    divides every element in the matrix by div
    Each row must have the same size, else return a ValueError
    Each element must be a number, else returns a ValueError

    Args:
        matrix: The numerical matrix
        div: The number to be divided by

    Returns:
        The matrix after the division

    Raises:
        ValueError if the row sizes are not equal or if a value is not a number
        ZeroDivisionError if div is 0
    """

    if div is 0:
        raise ZeroDivisionError("division by zero")
    div_matrix = []
    length = len(matrix[0])
    for i in matrix:
        div_list = []
        if length == len(i):
            length = len(i)
            for j in i:
                if not isinstance(j, (int, float)):
                    raise ValueError("matrix\
 must be a matrix (list of lists) of integers/floats")
                else:
                    div_list.append(round((j / div), 2))
            div_matrix.append(div_list)
        else:
            raise ValueError("Each row of the matrix must have the same size")
    return div_matrix
