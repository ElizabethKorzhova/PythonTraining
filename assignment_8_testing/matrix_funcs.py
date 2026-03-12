"""Module provides functions for working with matrix"""
import doctest
from typing import List


def matrix_multiply(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    """
    Multiplies two matrix
    :param matrix1: first matrix
    :param matrix2: second matrix
    :return: matrix multiplication result

    Examples:

    >>> matrix_multiply([[12, 7, 3], [4, 5, 6], [7, 8, 9]], [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]])
    [[114, 160, 60, 27], [74, 97, 73, 14], [119, 157, 112, 23]]
    >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    >>> matrix_multiply([[4, 2], [9, 0]], [[3, 1], [-3, 4]])
    [[6, 12], [27, 9]]
    >>> matrix_multiply([], [])
    []
    """
    return [[sum(m1 * m2 for m1, m2 in zip(rowM1, colM2))
             for colM2 in zip(*matrix2)] for rowM1 in matrix1]


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Transposes the given matrix
    :param matrix: matrix
    :return: transposed matrix

    Examples:

    >>> transpose_matrix([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    >>> transpose_matrix([[1, 2, 5, -1], [3, 4, 0, 0], [0, 0, 0 ,0]])
    [[1, 3, 0], [2, 4, 0], [5, 0, 0], [-1, 0, 0]]
    >>> transpose_matrix([[1, 2]])
    [[1], [2]]
    >>> transpose_matrix([[2], [4]])
    [[2, 4]]
    >>> transpose_matrix([[5]])
    [[5]]
    >>> transpose_matrix([])
    []
    """
    return list(map(list, zip(*matrix)))


if __name__ == '__main__':
    doctest.testmod()
