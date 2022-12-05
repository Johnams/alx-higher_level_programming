#!/usr/bin/python3
# 6-print_matrix_integer.py


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        i = 0
        for j in row:
            len_matrix = len(row)
            i += 1
            print("{:d}".format(j), end="")
            if i != len_matrix:
                print(" ", end="")
        print("")
