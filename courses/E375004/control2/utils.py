# utils.py

from sympy import symbols, Function, diff, simplify, sin, cos, solve, lambdify
import cloudpickle
import os


def initialize(cache_path="lambdified.pkl"):

    if os.path.exists(cache_path):
        with open(cache_path, 'rb') as f:
            funcs = cloudpickle.load(f)
            print("✅ Loaded lambdified functions from cache.")
            return funcs['x_ddot'], funcs['theta_ddot']


    # --- Symbolic Variables ---
    t = symbols('t')
    x = Function('x')(t)
    theta = Function('theta')(t)
    x_dot = diff(x, t)
    theta_dot = diff(theta, t)

    m, M, l, g, F, cx, ctheta = symbols('m M l g F cx ctheta')

    # --- Kinetic Energy ---
    T_cart = (1/2)*M*x_dot**2
    v_pend = x_dot + l * cos(theta) * theta_dot
    w_pend = l * sin(theta) * theta_dot
    T_pend = (1/2)*m * (v_pend**2 + w_pend**2)
    T = simplify(T_cart + T_pend)

    # --- Potential Energy ---
    V = -m * g * l * cos(theta)

    # --- Lagrangian ---
    L = T - V

    # --- Generalized Forces ---
    Q_x = F - cx * x_dot
    Q_theta = -ctheta * theta_dot

    # --- Euler-Lagrange Equations ---
    dL_dx = diff(L, x)
    dL_dx_dot = diff(L, x_dot)
    d_dt_dL_dx_dot = diff(dL_dx_dot, t)
    EL_x = simplify(d_dt_dL_dx_dot - dL_dx - Q_x)

    dL_dtheta = diff(L, theta)
    dL_dtheta_dot = diff(L, theta_dot)
    d_dt_dL_dtheta_dot = diff(dL_dtheta_dot, t)
    EL_theta = simplify(d_dt_dL_dtheta_dot - dL_dtheta - Q_theta)

    # --- Solve for accelerations ---
    sol = solve([EL_x, EL_theta], (diff(x, t, t), diff(theta, t, t)))
    x_ddot_expr = simplify(sol[diff(x, t, t)])
    theta_ddot_expr = simplify(sol[diff(theta, t, t)])

    # --- Lambdify ---
    vars = (x, x_dot, theta, theta_dot, F, m, M, l, g, cx, ctheta)
    x_ddot_func = lambdify(vars, x_ddot_expr)
    theta_ddot_func = lambdify(vars, theta_ddot_expr)

    # --- Save for later ---
    with open(cache_path, 'wb') as f:
        cloudpickle.dump({'x_ddot': x_ddot_func, 'theta_ddot': theta_ddot_func}, f)
        print("💾 Lambdified functions saved to cache.")


    return x_ddot_func, theta_ddot_func


def euler_step_cartpole(state, dt, t, external_force, x_ddot_func, theta_ddot_func, params):
    """
    Perform one step of Euler integration for the cart-pole system.

    Parameters:
        state (list): Current state of the system [x, x_dot, theta, theta_dot].
        dt (float): Time step for integration.
        t (float): Current time.
        external_force_func (function): Function to compute external force as a function of time.
        x_ddot_func (function): Function to compute the acceleration of the cart.
        theta_ddot_func (function): Function to compute the angular acceleration of the pole.
        params (dict): Dictionary of system parameters (e.g., mass, length, damping).

    Returns:
        list: Updated state of the system as a list in the format [x (position), x_dot (velocity), theta (angle), theta_dot (angular velocity)].
    """
    # Unpack state
    x, x_dot, theta, theta_dot = state 
 

    # Compute acceleration of the cart
    dx2 = x_ddot_func(x, x_dot, theta, theta_dot, external_force , **params) 

    # Compute angular acceleration of the pole
    dtheta2 = theta_ddot_func(x, x_dot, theta, theta_dot, external_force, **params) 
    
    # Euler integration step
    # Update x velocity and x position
    x_dot += dx2 * dt
    x += x_dot * dt

    # Update angular velocity and angle
    theta_dot += dtheta2 * dt
    theta += theta_dot * dt

    return [x, x_dot, theta, theta_dot]


class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        self.integral = 0.0
        self.prev_error = 0.0

    def reset(self):
        """Reset internal state (e.g. between episodes)."""
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, setpoint, measurement, dt):
        """Compute PID output for the current time step."""
        error = setpoint - measurement
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt if dt > 0 else 0.0
        self.prev_error = error

        output = (
            self.Kp * error +
            self.Ki * self.integral +
            self.Kd * derivative
        )
        return output
