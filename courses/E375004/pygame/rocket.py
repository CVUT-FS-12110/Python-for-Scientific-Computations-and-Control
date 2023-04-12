import pygame

from utils import boundaries
from utils import box
from utils import box_vendor

pygame.init()

# BASIC COLOURS (sometimes, it's usefull to define them as constants)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# FONTS
pygame.font.init()
myfont = pygame.font.SysFont('Arial',50)

# IMPORTANT GAME CONSTANTS
WIDTH = 800 # display widht
HEIGHT = 600 # display height
TICK = 100 # clock tick

GameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Rocket')
clock = pygame.time.Clock()

# LOADING OUR IMAGE OF ROCKET AND RESIZING IT
RESIZED = 300 # resized pixels of rocket img

rocketIMG = pygame.image.load('rocket.png')
rocketIMG = pygame.transform.scale(rocketIMG,(RESIZED, RESIZED))

# INITIALIZATION AND CALCULATION OF IMPORTANT VARIABLES
#   POSITION OF A ROCKET
x = int((WIDTH - RESIZED)/2) # initial coordinate x
y = int(HEIGHT - RESIZED + 50) # initial coordinate y + 50 pixels because of "good looking" grey trail
x_change = 0 # change of coordinate x in the beggining

# BOX VENDOR
SPEED = 1
VENDOR = box_vendor(
    num_boxes = 4,
    width = WIDTH,
    height = HEIGHT,
    a = 60,
    padding = 5
)

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
    
    # moving boxes with SPEED
    VENDOR.move_all(0, SPEED)
    VENDOR.update()

    if VENDOR.colision(rocket_hitbox_x, rocket_hitbox_y):
        print('Colision!')
    
    # GRAPHIC
    #   fill screen with white colour
    GameDisplay.fill(white)

    #   boxes
    VENDOR.draw(GameDisplay)

    #   hitbox of a rocket
    # pygame.draw.rect(
    #         GameDisplay,
    #         red,
    #         pygame.Rect((
    #             rocket_hitbox_x[0],
    #             rocket_hitbox_y[0],
    #             rocket_hitbox_x[1] - rocket_hitbox_x[0],
    #             rocket_hitbox_y[1] - rocket_hitbox_y[0]

    #         ))
    #     )

    #   show image of rocket in position x,y
    GameDisplay.blit(rocketIMG,(x,y))

    pygame.display.update()
    clock.tick(TICK)

pygame.quit()