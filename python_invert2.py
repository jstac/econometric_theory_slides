import numpy as np
from scipy.linalg import solve

A = [[0, 2, 4],
     [1, 4, 8],
     [0, 3, 6]]

b = (1, 2, 0)

A, b = np.asarray(A), np.asarray(b)

x = solve(A, b)
