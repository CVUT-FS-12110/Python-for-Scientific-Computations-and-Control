"""
Utility functions for pygame simulator ('simulator.py')
"""
import numpy as np
import matplotlib.pyplot as plt

def solver(x, v_x, c, m, f, delta_t, x_max, x_img_size, padding = 0):
    """
    Euler solver of dynamical system:

    m*x" + c*x' = f

    state space substitution:

    x1 = x
    x2 = v_x

    x1(k+1) = x1(k) + x2(k) * delta_t
    x2(k+1) = x2(k) + (-c/m * x2(k) + f(k)/m) * delta_t

    :param x: x position of simulated system [px]
    :param v_x: velocity in x direction of simulated system [px/s]
    :param c: damping parameter [kg/s]
    :param m: weight [kg]
    :param f: external force [N]
    :param delta_t: time step of the simulation [s]
    :param x_max: x boundary of pygame screen [px]
    :param x_img_size: image width [px]
    :param padding: pygame screen padding [px]
    :return: new x position and new x velocity
    """

    x_new = x + v_x*delta_t # new x position calculation
    v_new = v_x - (c / m) * v_x * delta_t + (f / m) * delta_t # new x velocity calculation

    # check boundaries. If the system is at the boundary then: x(k+1) = x(k) and new velocity is 0
    if x_new + x_img_size//2 +padding > x_max:
        return x, 0
    elif x_new + x_img_size//2 < 0:
        return x, 0
    else:
        return x_new, v_new

def controller():
    # TODO your own controller
    return 0

def update_line(plot, new_data, time_step):
    plot.set_xdata(np.append(plot.get_xdata(), new_data[0]))
    plot.set_ydata(np.append(plot.get_ydata(), new_data[1]))
    plt.draw()        # draw new data
    plt.pause(time_step)    # update graph every 0.5 second


