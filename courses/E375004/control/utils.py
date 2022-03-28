"""
Utility functions for pygame simulator ('simulator.py')
"""
import pygame
import random


def solver(x, v_x, damping , m, force, delta_t, x_max, x_img_size, padding = 0):
    x_new = x + v_x*delta_t # x1(k+1) = x1 + x2*delta_t
    v_new = v_x - (damping/m)*v_x*delta_t + (force/m)*delta_t # x2(k+1) = x2(k) (- c/m*x2 + F/m)*delta_t

    if x_new + x_img_size//2 +padding > x_max:
        return x, 0
    elif x_new + x_img_size//2 < 0:
        return x, 0
    else:
        return x_new, v_new
    
def boundaries(x, x_change, x_max, x_img_size, padding = 0):
    """
    Arguments:  x           - int, current positon of rocket
                x_change    - int, differnce in pixels
                x_img_size  - int, size of image in pixels
                padding     - int, optional, additional padding
    Returns:    int, new position of rocket
    """
    px = x + x_change
    if px + x_img_size//2 +padding > x_max:
        return x
    elif px + x_img_size//2 < 0:
        return x
    else:
        return px


class box:
    def __init__(self, coords, colour = (0, 0, 0)):
        """
        Box constructor
        Arguments:  coords - tuple of 4 intigers (x, y, range_x, range_y)
                    colour - optional, default is black - colour of box
        Returns:    box
        """
        # COORDINATES OF A BOX
        self.coordinates = coords
        # CALCULATION OF HITBOX FOR X AND Y
        self.hitbox_x = (
            self.coordinates[0],
            self.coordinates[0] + self.coordinates[2]
        )
        self.hitbox_y = (
            self.coordinates[1],
            self.coordinates[1] + self.coordinates[3]
        )
        # COLOUR OF A BOX
        self.colour = colour

    def move(self, move_x, move_y):
        """
        Arguments:  move_x  - int, pixels
                    move_y  - int, pixels
        Returns:    None
        Notes:      Moves square move_x pixels in x axis
                    and move_y pixels in y axis
        """
        # UPDATING COORDINATES
        self.coordinates = (
            self.coordinates[0] + move_x,
            self.coordinates[1] + move_y,
            self.coordinates[2],
            self.coordinates[3]
        )
        # UPDATING HITBOX FOR X AND Y
        self.hitbox_x = (
            self.coordinates[0],
            self.coordinates[0] + self.coordinates[2]
        )
        self.hitbox_y = (
            self.coordinates[1],
            self.coordinates[1] + self.coordinates[3]
        )

    def colision(self, hitbox_x, hitbox_y):
        """
        Arguments:  hitbox_x - tuple, coordinates of x axis of hitbox
                    hitbox_y - tuple, coordinates of y axis of hitbox
        Returns:    boolean - if hitboxes are in colision returns True
        """
        if max(hitbox_x) < min(self.hitbox_x) or max(self.hitbox_x) < min(hitbox_x):
            x = False
        else:
            x = True
        if max(hitbox_y) < min(self.hitbox_y) or max(self.hitbox_y) < min(hitbox_y):
            y = False
        else:
            y = True        
        return x and y
    
    def down_check(self, height):
        """
        Arguments:  height  - int, pixels, height of a screen
        Returns:    boolean - if it should be deleted
        """
        if self.coordinates[1] > height:
            return True
        else:
            return False

    def draw(self, display):
        """
        Arguments:  display -   pygame.screen
        Returns:    None
        Notes:      Function draws square on a display
        """
        pygame.draw.rect(
            display,
            self.colour,
            pygame.Rect(self.coordinates)
        )


class box_vendor:
    def __init__(self, num_boxes, width, height, a = 60, padding = 5):
        """
        box_vendor constructor
        Arguments:  num_boxes   - int, number of boxes
                    width       - int, width of screen in pixels
                    height      - int, height of screen in pixels
                    a           - int, optional, default is 60
                                  range of x and y of all boxes
                    padding     - int, optional, default is 5
                                  padding for box creation
        Returns>    box_vendor
        """
        # IMPORTANT CONSTANTS
        self.num_boxes = num_boxes
        self.width = width
        self.height = height
        self.a = a
        self.padding = padding
        self.box_container = []
        # CREATING BOXES IN RANDOM POSITION IN THE TOP THIRD OF A SCREEN
        for _ in range(num_boxes):
            coords = (
                random.randint(0 + self.padding, self.width - self.padding - self.a),
                random.randint(0 , (self.height - self.padding - self.a) // 3),
                self.a,
                self.a
            )
            self.box_container.append(box(coords))

    def move_all(self, move_x, move_y):
        """
        Arguments:  move_x  - int, pixels
                    move_y  - int, pixels
        Returns:    None
        Notes:      Moves all boxes move_x pixels in 
                    x axis and move_y pixels in y axis
        """
        for elem in self.box_container:
            elem.move(move_x, move_y)
    
    def update(self):
        """
        Arguments:  ---
        Returns:    None
        Notes:      Updates our box vendor, removes all boxes
                    lower then our screen and creates a new
                    ones at the top.
        """
        for k in range(self.num_boxes):
            if self.box_container[k].down_check(self.height):
                coords = (
                    random.randint(0 + self.padding, self.width - self.padding - self.a),
                    0,
                    self.a,
                    self.a
                )
                self.box_container[k] = box(coords)
            else:
                pass
    
    def colision(self, hitbox_x, hitbox_y):
        """
        Arguments:  hitbox_x - tuple, coordinates of x axis of hitbox
                    hitbox_y - tuple, coordinates of y axis of hitbox
        Returns:    boolean - if hitboxes are in colision returns True
        TO DO:      Simplify that ugly code!
        """
        returned = False
        for elem in self.box_container:
            if elem.colision(hitbox_x, hitbox_y):
                returned = returned or True
        return returned
            
    def draw(self, display):
        """
        Arguments:  display - pygame.screen
        Returns:    None
        Notes:      Displayes all boxes on display
        """
        for elem in self.box_container:
            elem.draw(display)
