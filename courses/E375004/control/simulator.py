"""
Simple control simulation
"""
import pygame
import matplotlib.pyplot as plt
import random

from utils import solver, controller, update_line

# IMPORTANT GAME CONSTANTS
WIDTH = 800 # display widht
HEIGHT = 600 # display height
TICK = 40 # framerate: frames per second
GAME_CAPTION = "Control simulation"
RESIZED = 200 # pixels of rocket IMG
ROCKET_IMG_PATH = "rocket.png"


# BASIC COLOURS
# It's usefull to define them as constants, we can use
# them reapeatedly
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

if __name__ == "__main__":
    # initialize updating plot
    plot, = plt.plot([], [])  # empty plot
    # set axis limits
    plt.xlim(0, 30) # 30 seconds of simulation will be visualized
    plt.ylim(0, WIDTH) # the range of x position will be visualized
    # title, labels
    plt.title("x position of the rocket in time")
    plt.xlabel("time [s]")
    plt.ylabel("x position [px]")

    pygame.init() # inits all important pygame modules for us
    pygame.font.init() # fonts
    myfont = pygame.font.SysFont('Arial',50)

    game_display = pygame.display.set_mode((WIDTH, HEIGHT)) # create game display
    pygame.display.set_caption(GAME_CAPTION) # set caption
    clock = pygame.time.Clock() # initilize clock

    # Load and prepare our image of rocket
    rocket_img = pygame.image.load(ROCKET_IMG_PATH)
    rocket_img = pygame.transform.scale(rocket_img,(RESIZED, RESIZED))
    rocket_img = pygame.transform.rotate(rocket_img, 90) # rotate img 90 degrees

    # Initial position of a rocket - bottom center
    x = int((WIDTH - RESIZED)/2) # initial coordinate x
    y = int(HEIGHT - RESIZED - 200) # initial coordinate y

    # initial conditions
    force = 0 # initial force is zero
    max_wind_force = 30  # maximum wind disturbance force [N]
    velocity = 0 # initial velocity
    delta_t = 1/TICK #time step of simulation = 1/framerate

    # parameters of controlled system
    weight = 1 # weight [kg]
    damping = 0.5 #damping parameter [kg/s]
        
    
    # main while loop
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                crashed = True # if we pressed cross, game will end
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    force = -50
                elif event.key == pygame.K_RIGHT:
                    force = 50

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    force = 0

        # random force disturbance
        force_disturbance = random.uniform(0, max_wind_force)



        # TODO program your own controller
        # force = controler()

        # sum of controlling force and force disturbance
        total_force = force + force_disturbance

        # call the solver - calculate x position and velocity
        x, velocity = solver(x, velocity, damping, weight, total_force, delta_t, WIDTH, RESIZED)
                
        # GRAPHIC
        #   fill screen with white colour
        game_display.fill(WHITE)


        # show image of rocket in position x,y
        game_display.blit(rocket_img,(x,y))
        pygame.display.update()

        # update the graph
        simulation_time = pygame.time.get_ticks()/1000 # get simulation time in seconds
        update_line(plot, [simulation_time, x], delta_t)

        clock.tick(TICK)

    pygame.quit()   
