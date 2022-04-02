import pygame,sys
from sprites import *
from config import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(display_size)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill(bg_colour)

	clock.tick(fps)
	pygame.display.flip()