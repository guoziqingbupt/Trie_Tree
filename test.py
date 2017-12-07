import numpy as np


M1 = np.array([[4, 0, 1], [1, 4, 2], [1, 4, 3]])
M2 = np.array([[3, 0, 0], [2, 4, 4], [0, 1, 4]])

I11 = np.array([1, -0.5, 0.2])
I12 = np.array([1, 0.5, 0.8])

Q11 = np.array([0.3, 1, 0])
Q12 = np.array([0.7, 1, 0])

x1 = np.transpose(M1) @ I11
x2 = np.transpose(M2) @ I12
x3 = np.linalg.inv(M1) @ Q11
x4 = np.linalg.inv(M2) @ Q12


print(np.inner(x1, x3) + np.inner(x2, x4))