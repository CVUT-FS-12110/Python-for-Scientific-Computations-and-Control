import sympy as sp
import numpy as np
from scipy.integrate import ode
import matplotlib.pyplot as plt
# import time

# SymPy derivation

## time
t = sp.symbols("t")

## generalized coordinates
s = sp.Function("s")(t)
theta = sp.Function("theta")(t)

q = sp.Matrix([s, theta])

## properties
g, l, m_c, m_p = sp.symbols("g, l m_c m_p")

## velocity of the mass
xdot_p = sp.diff(s, t) + sp.diff(theta, t) * l * sp.cos(theta)
ydot_p = sp.diff(theta, t) * l * sp.sin(theta)

## kinetic and potential energy
T = 0.5 * m_c * sp.diff(s, t) ** 2 + 0.5 * m_p * (xdot_p**2 + ydot_p**2)
V = g * m_p * l * sp.cos(theta)

## terms of EoM
mass_matrix = sp.hessian(T, sp.diff(q, t))  # M
bias_terms = sp.diff(T, sp.diff(q, t).T).jacobian(q) * sp.diff(q, t) - sp.diff(T, q)  # c
potential_terms = -sp.diff(V, q)  # tau_g

## printout
print(sp.simplify(mass_matrix))
print(sp.simplify(bias_terms))
print(sp.simplify(potential_terms))

# Conversion to numpy functions

## terms with substituted parameters
substitutions = [(g, 9.81), (l, 1), (m_c, 5), (m_p, 7)]

mass_matrix_subs = mass_matrix.subs(substitutions)
bias_terms_subs = bias_terms.subs(substitutions)
potential_terms_subs = potential_terms.subs(substitutions)

## numpy functions
mass_matrix_num = sp.lambdify((q,), mass_matrix_subs, "numpy")
bias_terms_num = sp.lambdify((q, sp.diff(q, t)), bias_terms_subs, "numpy")
potential_terms_num = sp.lambdify((q,), potential_terms_subs, "numpy")

## comparison of substitution's and numpy function's evaluation times
# q_bench = np.array([0, np.pi / 4])
# qdot_bench = np.array([0, 0])

# st = time.time()
# mass_matrix.subs([(s, q_bench[0]), (theta, q_bench[1])])
# bias_terms.subs(
#     [
#         (s, q_bench[0]),
#         (theta, q_bench[1]),
#         (sp.diff(s, t), qdot_bench[0]),
#         (sp.diff(theta, t), qdot_bench[1]),
#     ]
# )
# potential_terms.subs([(s, q_bench[0]), (theta, q_bench[1])])
# et = time.time()
# print("substitution: ", et - st, "s")

# st = time.time()
# mass_matrix_num(q_bench)
# bias_terms_num(q_bench, qdot_bench)
# potential_terms_num(q_bench)
# et = time.time()
# print("numpy: ", et - st, "s")

# Simulation


## qddot (acceleration)
def acceleration(q, qdot):
    return np.linalg.solve(
        mass_matrix_num(q),
        -bias_terms_num(q, qdot) + potential_terms_num(q),
    )


## state space representation
def dynamics(_, x):
    q = x[0:2]
    qdot = x[2:4]
    return np.concatenate((qdot, np.reshape(acceleration(q, qdot), (2))))


solver = ode(dynamics).set_integrator("dopri5")

t0 = 0.0
y0 = np.array([0, np.pi / 4, 0, 0])
t1 = 10.0

solver.set_initial_value(y0, t0)
t_values = [t0]
y_values = [y0]

while solver.successful() and solver.t < t1:
    solver.integrate(solver.t + 1e-1)
    t_values.append(solver.t)
    y_values.append(solver.y)

## visualization
plt.plot(t_values, [x[0] for x in y_values])
plt.plot(t_values, [x[1] for x in y_values])
plt.show()
