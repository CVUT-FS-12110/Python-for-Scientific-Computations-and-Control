import pygame
import math
import numpy as np
import utils  # <- make sure it includes PIDController and symbolic model

# --- Initialize symbolic model ---
x_ddot_func, theta_ddot_func = utils.initialize()

# --- Parameters in meters, kg ---
params = {
    'm': 0.1,
    'M': 1.0,
    'l': 1.5,
    'g': 9.81,
    'cx': 0.1,
    'ctheta': 0.005
}

px_per_meter = 100

# --- Initial state: [x, x_dot, theta, theta_dot] ---
state = [3.0, 0.0, 0*math.pi - 0.1, 0.0]  # slightly offset pendulum
t = 0.0

# --- PID Controllers ---
outer_pid = utils.PIDController(Kp=3, Ki=0.1, Kd=3)     # x → θ̇_target
middle_pid = utils.PIDController(Kp=-0.03, Ki=0.0, Kd=-0.02)    # θ̇_target → θ_target
inner_pid = utils.PIDController(Kp=-10, Ki=0.0, Kd=-5) # θ_target → force

# --- Target ---
target_position = 5.0  # meters (centered)

# --- PyGame Setup ---
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hierarchical PID Control: Cart-Pole Crane")
clock = pygame.time.Clock()

# --- Render constants ---
cart_width_px = 100
cart_height_px = 30
bob_radius = 10
origin_y_px = height // 2

# --- Main Loop ---
running = True
while running:
    # --- Real-time dt ---
    dt_ms = clock.tick(60)
    dt = dt_ms / 1000
    t += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # 3-layer hierarchical control
    # theta_dot_target = outer_pid.update(target_position, state[0], dt)
    theta_target = -0.05*middle_pid.update(0, state[3], dt)
    # applied_force = inner_pid.update(0, state[3], dt)
    applied_force = 1*outer_pid.update(target_position, state[0], dt) + inner_pid.update(2*math.pi + theta_target, state[2], dt)

    def force_func(_t): return applied_force

    # --- Euler Integration Step ---
    state = utils.euler_step_cartpole(state, dt, t, force_func, x_ddot_func, theta_ddot_func, params)

    # --- Unpack state (in meters/radians) ---
    cart_x_m, _, theta, _ = state
    cart_y_px = origin_y_px

    # --- Convert to pixels for drawing ---
    cart_x_px = int(cart_x_m * px_per_meter)
    draw_l = params['l'] * px_per_meter

    pendulum_x_px = cart_x_px + draw_l * math.sin(theta)
    pendulum_y_px = cart_y_px + draw_l * math.cos(theta)

    # --- Render ---
    screen.fill((255, 255, 255))

    # Draw cart
    cart_rect = pygame.Rect(
        cart_x_px - cart_width_px // 2,
        cart_y_px - cart_height_px // 2,
        cart_width_px,
        cart_height_px
    )
    pygame.draw.rect(screen, (0, 0, 0), cart_rect)
    pygame.draw.line(screen, (180, 180, 180), (cart_x_px, cart_y_px), (pendulum_x_px, pendulum_y_px), 4)
    pygame.draw.circle(screen, (200, 0, 0), (int(pendulum_x_px), int(pendulum_y_px)), bob_radius)

    pygame.display.flip()

pygame.quit()
