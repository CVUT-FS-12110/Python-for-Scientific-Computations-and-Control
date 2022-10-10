"""
Pygame example

Do no use jupyter notebook. Call this code from console (or any IDE you like).
"""

import time
import pygame
import os
import numpy as np
from pygame import gfxdraw


class Item():

	def __init__(self, position, speed):
		self.mx, self.my = position
		self.mx_1, self.my_1 = self.mx, self.my
		self.vx, self.vy = speed
		self.vx_1, self.vy_1 = self.vx, self.vy
		rc = int(abs(vx / 3. * 255))
		gc = int(abs(vy / 3. * 255))
		bc = 0 # np.random.randint(0, 255)
		self.color = (rc, gc, bc) 
		self.list_x = np.array([])
		self.list_y = np.array([])

		self.list_x_1 = np.array([])
		self.list_y_1 = np.array([])

	def update(self):
		self.vx = (0.999 * self.vx)
		self.vy = (0.999 * self.vy) + 0.003

		self.mx += self.vx
		self.my += self.vy

		if self.my >= GROUND_LEVEL:
			self.vy = -0.8 * self.vy
			#self.vy = 0
			self.vx = 0.5 * self.vx
			self.my = GROUND_LEVEL

		pygame.draw.circle(screen, self.color, (int(self.mx), int(self.my)), 20)

		self.list_x_1 = np.append(self.list_x_1, self.mx)
		self.list_y_1 = np.append(self.list_y_1, self.my)




WINDOW_X = 0
WINDOW_Y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (WINDOW_X, WINDOW_Y)

WIDTH = 1000
HEIGHT = 700
GROUND_LEVEL = HEIGHT - 50

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

done = False

mx = 50
my = GROUND_LEVEL


items = []
for idx in range(10):
	vy = -np.random.random() * 3
	vx = np.random.random() * 3
	item = Item((mx, my), (vx, vy))
	items.append(item)


while not done:
	screen.fill((0, 0, 0))
	pygame.draw.line(screen, (150, 75, 0), (0, GROUND_LEVEL), (WIDTH, GROUND_LEVEL), 10)

	for item in items:
		item.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				done = True

	time.sleep(0.01)
	pygame.display.flip()