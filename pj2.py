# The Inverse Power Method
import numpy as np


def Inverse_power_method(matrix, x, max_iterations=1000, diff=0.00001):
    estimate = 3.3

    prev_u = float("inf")

    for iteration in range(max_iterations):
        # (A - 3.3I)y Solve
        x = np.linalg.solve(matrix - estimate * np.identity(matrix.shape[0]), x)

        u = max(x)

        v = estimate + 1 / u

        x /= u

        if np.abs(u - prev_u) < diff:
            return v

        prev_u = u


# 초기 설정
MATRIX = np.array([[10, -8, -4], [-8, 13, 4], [-4, 5, 4]])
x = np.array([1, 1, 1])

eigenvalue = Inverse_power_method(MATRIX, x)
print(eigenvalue)
