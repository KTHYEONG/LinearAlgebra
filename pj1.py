# Iterative power method

import numpy as np


def iterative_power_method(matrix):
    n = matrix.shape[0]


MATRIX = np.array([[6, 1], [5, 2]])

eigenvalue = iterative_power_method(MATRIX)
