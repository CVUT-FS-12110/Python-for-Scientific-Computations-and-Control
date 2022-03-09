"""
Simple rocket game simulator
"""
import pygame

from utils import boundaries, box_vendor

# IMPORTANT GAME CONSTANTS
WIDTH = 800 # display widht
HEIGHT = 600 # display height
TICK = 100 # clock tick [ms]
GAME_CAPTION = "Space Rocket 2D Game"
RESIZED = 300 # pixels of rocket IMG
ROCKET_IMG_PATH = "rocket.png"
SHOW_ROCKET_HITBOX = True

# BOX Vendor
BOX_SPEED = 1
NUM_BOXES = 8

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
    x_change = 0 # change of coordinate x in the beggining

    # Box Vendor
    VENDOR = box_vendor(num_boxes=NUM_BOXES, width=WIDTH, height=HEIGHT,
                        a=60, padding=5)

    # main while loop
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                crashed = True # if we pressed cross, game will end
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        x = boundaries(x, x_change, WIDTH, RESIZED) # updatting position of a rocket (axis x)
        rocket_hitbox_x = (
            int(x + RESIZED / 2) - 25,
            int(x + RESIZED / 2) + 25
        ) # calculating new rocket hitbox x
        rocket_hitbox_y = (
            y + 10,
            y + 170
        ) # calculating new rocket hitbox y
        
        # moving boxes with specified BOX_SPEED
        VENDOR.move_all(0, BOX_SPEED)
        VENDOR.update()

        if VENDOR.colision(rocket_hitbox_x, rocket_hitbox_y):
            print('Colision!')
        
        # GRAPHIC
        #   fill screen with white colour
        game_display.fill(white)

        #   boxes
        VENDOR.draw(game_display)

        #   hitbox of a rocket
        if SHOW_ROCKET_HITBOX:
            pygame.draw.rect(
                    game_display,
                    red,
                    pygame.Rect((
                        rocket_hitbox_x[0],
                        rocket_hitbox_y[0],
                        rocket_hitbox_x[1] - rocket_hitbox_x[0],
                        rocket_hitbox_y[1] - rocket_hitbox_y[0]

                    ))
                )

        # show image of rocket in position x,y
        game_display.blit(rocket_img,(x,y))

        pygame.display.update()
        clock.tick(TICK)

    pygame.quit()   