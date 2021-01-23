import pygame
from globals import path, screen

grass_image = pygame.image.load(f'{path}/assets/grass.png')
dirt_image = pygame.image.load(f'{path}/assets/dirt.png')

grass_image = pygame.transform.scale(grass_image, (64, 64))
dirt_image = pygame.transform.scale(dirt_image, (64, 64))

TILE_SIZE = grass_image.get_width()

level_1 = \
[['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','2'],
['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1','1'],
['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

class Level:
	def __init__(self, level_map):
		self.level_map = level_map
		self.tile_rects = []

	def render(self):
		self.tile_rects = []
		y = 0
		for row in self.level_map:
			x = 0
			for tile in row:
				if tile == '1':
					screen.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
				if tile == '2':
					screen.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
				if tile != '0':
					self.tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
				x += 1
			y += 1

	def collision_test(self, rect, tiles):
		hit_list = []
		for tile in tiles:
			if rect.colliderect(tile):
				hit_list.append(tile)
		return hit_list
