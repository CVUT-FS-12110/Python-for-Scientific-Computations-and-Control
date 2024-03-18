import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

# Discrete time state-space representation
dt = 1e-2
A = np.eye(4) + np.array([[0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]]) * dt
B = np.array([[0, 0], [0, 0], [1, 0], [0, 1]]) * dt

# Optimal control problem
N = 100  # MPC horizon
M = 1000  # total number of steps

x0 = np.array([2, 1, 0, 0])  # initial state
u_max = 2  # symmetric upper and lower bound on inputs

Q = 1e0 * np.eye(4)
R = 1e-2 * np.eye(2)

# CVXPY model of the MPC problem
## variables and parameters
x = cp.Variable((4, N + 1))
u = cp.Variable((2, N))
x_init = cp.Parameter(4)

## constraints and cost
constraints = [
    x[:, 0] == x_init,
    x[:, 1:N] == A @ x[:, 0 : N - 1] + B @ u[:, 0 : N - 1],
    -u_max <= u,
    u <= u_max,
]
cost = cp.sum_squares(np.sqrt(Q) @ x) + cp.sum_squares(np.sqrt(R) @ u)

## problem
prob = cp.Problem(cp.Minimize(cost), constraints)

# MPC simulation
## pre-allocation
xs = np.empty((4, M + 1))
us = np.empty((2, M))

## initial state
xs[:, 0] = x0

## simulaation loop
for i in range(M):
    x_init.value = xs[:, i]  # current state assigned as first MPC state
    prob.solve(solver=cp.OSQP)  # MPC optimization

    us[:, i] = u.value[:, 0]  # first MPC input assigned as current input
    noise = np.random.uniform(-1, 1, 2)  # random input noise

    xs[:, i + 1] = A @ xs[:, i] + B @ (us[:, i] + noise)  # next state

# Visualization
plt.subplot(2, 1, 1)
for i in range(4):
    plt.plot(xs[i, :], label=f"x{i+1}")
plt.legend()

plt.subplot(2, 1, 2)
for i in range(2):
    plt.plot(us[i, :], label=f"u{i+1}")
plt.legend()

plt.show()
