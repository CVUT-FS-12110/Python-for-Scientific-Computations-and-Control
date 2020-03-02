"""
Pygame example

Do no use jupyter notebook. Call this code from console (or any IDE you like).
"""

import time
import pygame
import os
import numpy as np

WINDOW_X = 0
WINDOW_Y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (WINDOW_X, WINDOW_Y)

WIDTH = 1000
HEIGHT = 700

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

done = False

while not done:
	screen.fill((0, 0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	time.sleep(0.01)
	pygame.display.flip()