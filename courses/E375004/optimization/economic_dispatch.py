import osqp
import numpy as np
from scipy.sparse import csc_matrix

Q = csc_matrix([[0.02, 0, 0], [0, 0.015, 0], [0, 0, 0.01]])
q = np.array([5, 4, 3])

A = csc_matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]])
l = np.array([200, 300, 100, 3000])
u = np.array([1000, 1500, 800, 3000])

# solution
m = osqp.OSQP()
m.setup(P=Q, q=q, A=A, l=l, u=u, polish=True)
result = m.solve()

# results
print("x = ", result.x)
