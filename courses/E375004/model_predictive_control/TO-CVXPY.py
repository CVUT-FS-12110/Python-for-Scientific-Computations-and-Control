import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

# Discrete time dynamics
h = 1e-2
A = np.eye(4) + np.array([[0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]]) * h
B = np.array([[0, 0], [0, 0], [1, 0], [0, 1]]) * h

# Trajectory optimization problem
N = 1000

x0 = np.array([2, 1, 0, 0])
u_max = 2

Q = 1e0 * np.eye(4)
R = 1e-2 * np.eye(2)

# CVXPY model of the TO problem
## variables and parameters
x = cp.Variable((4, N + 1))
u = cp.Variable((2, N))

## cost and constraints
state_cost = sum([cp.quad_form(x[:, i], Q) for i in range(N + 1)])
input_cost = sum([cp.quad_form(u[:, i], R) for i in range(N)])
objective = cp.Minimize(state_cost + input_cost)

constraints = [
    x[:, 0] == x0,
    x[:, 1:N] == A @ x[:, 0 : N - 1] + B @ u[:, 0 : N - 1],
    u <= u_max,
    u >= -u_max,
]

## problem
problem = cp.Problem(objective, constraints)

## solution
problem.solve()

# Visualization
plt.subplot(2, 1, 1)
for i in range(4):
    plt.plot(x.value[i, :])

plt.subplot(2, 1, 2)
for i in range(2):
    plt.plot(u.value[i, :])

plt.show()
