import pygame
from config import *

class Level:
	def __init__(self,level_map):
		self.display_surface = pygame.display.get_surface()

		self.background = pygame.image.load("Images/Carl.png").convert()

		self.all_sprites = pygame.sprite.Group()
		self.collision_sprites = pygame.sprite.Group()
		self.active_sprites = pygame.sprite.Group()
		self.visible_sprites = CameraGroup()

		self.setup_level(level_map)

	def setup_level(self,level_map):
		for i,row in enumerate(level_map):
			for j,val in enumerate(row):
				if val == "P":
					self.player = Player()

	def run(self):
		self.active_sprites.update()
		self.visible_sprites.cdraw(self.player)

class CameraGroup(pygame.sprite.Group):
	def __init__(self,player):
		pass

class Player(pygame.sprite.Sprite):
	def __init__(self,level_map):
		pass

class Block(pygame.sprite.Sprite):
	def __init__(self,level_map):
		pass
