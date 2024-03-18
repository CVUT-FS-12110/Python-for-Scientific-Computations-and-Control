import cvxpy as cp
import numpy as np

x = cp.Variable(9)

objective = cp.Maximize(x[7] + x[8])

u = np.array([5, 10, 8, 6, 2, 4, 5, 8, 9])

constraints = [
    x >= np.zeros(9),
    x <= u,
    x[3] + x[4] == x[1],
    x[5] + x[6] == x[2],
    x[7] == x[0] + x[3] + x[5],
    x[8] == x[4] + x[6]
]

problem = cp.Problem(objective,constraints)

problem.solve()
print(x.value)
print(objective.value)
