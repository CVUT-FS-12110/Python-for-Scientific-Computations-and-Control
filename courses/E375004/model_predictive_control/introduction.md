# Model Predictive Control

$$
\begin{aligned}
	\min_{\{\mathbf{x}_k\}_1^{N+1}, \{\mathbf{u}_k\}_0^{N}} & \quad \mathbf{x}_k^\top \mathbf{Q} \mathbf{x}_k + \mathbf{u}_k^\top \mathbf{R} \mathbf{u}_k \\
	\text{s.t.} & \quad \mathbf{x}_{k+1} = \mathbf{A} \mathbf{x}_k + \mathbf{B} \mathbf{u}_k \\
							& \quad \mathbf{u}_{\min} \leq \mathbf{u}_k \leq \mathbf{u}_{\max} \,,
\end{aligned}
$$

## 2-DOF double integrator

Let control a 2-DOF double integrator with an MPC controller with a prediction horizon of one second and quadratic running cost penalizing the state-error and input level.

We will use the first order approximation

$$
\mathbf{x}_{k+1} = \underbrace{(\mathbf{I} + \mathbf{A}_c h)}_{\mathbf{A}} \mathbf{x}_k + \underbrace{\mathbf{B}_c h}_{\mathbf{B}} \, \mathbf{u}_k 
$$

with a timestep of $10^{-2}$s to discretize its continuous dynamics

$$
\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x},\mathbf{u}) =
\underbrace{\begin{bmatrix}
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}}_{\mathbf{A}_c}
\mathbf{x}
+
\underbrace{\begin{bmatrix}
0 & 0 \\
0 & 0 \\
1 & 0 \\
0 & 1 \\
\end{bmatrix}}_{\mathbf{B}_c}
\mathbf{u}
\,.
$$

We will formulate the running cost as

$$
l(\mathbf{x}_k,\mathbf{u}_k) = \mathbf{x}_k^\top \mathbf{Q} \, \mathbf{x}_k + \mathbf{u}_k^\top \mathbf{R} \, \mathbf{u}_k
$$

and place additional constraints

$$
-2 \leq \mathbf{u}_k \leq 2
$$

on the controllers inputs.


### Code
- [CVXPY](MPC-CVXPY.py)

