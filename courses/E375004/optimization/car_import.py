import cvxpy as cp

x = cp.Variable(2, integer=True)

objective = cp.Maximize(x[0] * 0.25 + x[1] * 0.075)
constraints = [
	x >= 0,
    x[0] * 2.5 + x[1] * 0.45 <= 50,
    x[0] + x[1] <= 60
]

problem = cp.Problem(objective, constraints)
problem.solve(solver=cp.SCIP)

print("x = ", x.value)
print("f(x) = ", problem.value)
