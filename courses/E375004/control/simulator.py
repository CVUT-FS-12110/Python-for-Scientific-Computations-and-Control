"""
Simple rocket game simulator
"""
import pygame

from utils import solver, box_vendor

# IMPORTANT GAME CONSTANTS
WIDTH = 800 # display widht
HEIGHT = 600 # display height
TICK = 40 # framerate frames per second
GAME_CAPTION = "Control simulation"
RESIZED = 300 # pixels of rocket IMG
ROCKET_IMG_PATH = "rocket.png"
SHOW_ROCKET_HITBOX = True


# BASIC COLOURS
# It's usefull to define them as constants, we can use
# them reapeatedly
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

if __name__ == "__main__":
    pygame.init() # inits all important pygame modules for us
    pygame.font.init() # fonts
    myfont = pygame.font.SysFont('Arial',50)

    game_display = pygame.display.set_mode((WIDTH, HEIGHT)) # create game display
    pygame.display.set_caption(GAME_CAPTION) # set caption
    clock = pygame.time.Clock() # initilize clock

    # Load and prepare our image of rocket
    rocket_img = pygame.image.load(ROCKET_IMG_PATH)
    rocket_img = pygame.transform.scale(rocket_img,(RESIZED, RESIZED))

    # Initial position of a rocket - bottom center
    x = int((WIDTH - RESIZED)/2) # initial coordinate x
    y = int(HEIGHT - RESIZED + 50) # initial coordinate y + 50 pixels because of "good looking" grey trail
    force = 0 # change of coordinate x in the beggining
    v_x = 0 # initial velocity
    delta_t = 1/TICK

    m = 1 # weight [kg]
    c = 0.5 #damping parameter [TODO]
        
    
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
        
        x, v_x = solver(x, v_x, c, m, force, delta_t, WIDTH, RESIZED) # updatting position of a rocket (axis x)
                
        # GRAPHIC
        #   fill screen with white colour
        game_display.fill(white)



        # show image of rocket in position x,y
        game_display.blit(rocket_img,(x,y))

        pygame.display.update()
        clock.tick(TICK)

    pygame.quit()   
