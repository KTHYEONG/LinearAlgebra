# The Inverse Power Method
import numpy as np


def iterative_power_method(matrix, x, max_iterations=1000, diff=0.00001):
    prev_u = float("inf")

    for iteration in range(max_iterations):
        x = np.dot(matrix, x) - 0.0
        print(x)
        u = max(x)
        x /= u

        print(x)
        print(u)
        if np.abs(u - prev_u) < diff:
            return u
            break

        prev_u = u


# 초기 설정
MATRIX = np.array([[6, 5], [1, 2]])
x = np.array([0, 1])

eigenvalue = iterative_power_method(MATRIX, x)
print(eigenvalue)
