import pygame
import math
import numpy as np
import utils  # your file with symbolic model & euler step

# --- Initialize Symbolic Model ---
x_ddot_func, theta_ddot_func = utils.initialize()

# --- System Parameters (meters, kg, N) ---
params = {
    'm': 0.1,       # pendulum mass [kg]
    'M': 1.0,       # cart mass [kg]
    'l': 1.5,       # pendulum length [m]
    'g': 9.81,      # gravity [m/s^2]
    'cx': 0.1,      # cart damping
    'ctheta': 0.05  # pendulum damping
}

# --- Pixel rendering scale ---
px_per_meter = 100

# --- Initial State: [x, x_dot, theta, theta_dot] ---
state = [4.0, 0.0, 1*math.pi - 0.1, 0.0]  # x in meters
t = 0.0

# --- External force (interactive) ---
def external_force(time):
    return 0.0  # gets overridden

# At the top
pid = utils.PIDController(Kp=3, Ki=0.1, Kd=1)
pid_phi = utils.PIDController(Kp=10, Ki=0.1, Kd=5)
target_position = 5  # desired position of the cart


# --- PyGame Setup ---
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Crane with Load Simulation")
clock = pygame.time.Clock()

# --- Rendering Constants ---
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

    # --- Controls (applied force) ---
    keys = pygame.key.get_pressed()
    applied_force = pid.update(target_position, state[0], dt)

    
    if keys[pygame.K_LEFT]:
        applied_force += -10.0
    elif keys[pygame.K_RIGHT]:
        applied_force += 10.0


    def force_func(_t): return applied_force

    # --- Euler Simulation Step (meters) ---
    state = utils.euler_step_cartpole(state, dt, t, force_func, x_ddot_func, theta_ddot_func, params)

    # --- Unpack state (in meters/radians) ---
    cart_x_m, _, theta, _ = state
    cart_y_px = origin_y_px

    # --- Convert to pixels for drawing ---
    cart_x_px = int(cart_x_m * px_per_meter)
    draw_l = params['l'] * px_per_meter

    pendulum_x_px = cart_x_px + draw_l * math.sin(theta)
    pendulum_y_px = cart_y_px + draw_l * math.cos(theta)

    # --- Draw Scene ---
    screen.fill((255, 255, 255))  # background

    # Draw cart
    cart_rect = pygame.Rect(
        cart_x_px - cart_width_px // 2,
        cart_y_px - cart_height_px // 2,
        cart_width_px,
        cart_height_px
    )
    pygame.draw.rect(screen, (0, 0, 0), cart_rect)

    # Draw pendulum
    pygame.draw.line(screen, (180, 180, 180), (cart_x_px, cart_y_px), (pendulum_x_px, pendulum_y_px), 4)
    pygame.draw.circle(screen, (200, 0, 0), (int(pendulum_x_px), int(pendulum_y_px)), bob_radius)

    # --- Flip Frame ---
    pygame.display.flip()

    # Optional: print FPS
    # print(f"FPS: {clock.get_fps():.1f}")

pygame.quit()
