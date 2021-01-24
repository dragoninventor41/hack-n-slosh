import pygame
import pytmx
from globals import path, screen

# TILE_SIZE = grass_image.get_width()
TILE_SIZE = 64

level_1 = pytmx.load_pygame(f'{path}/blursed_level.tmx')

class Level:
	def __init__(self, level):
		self.level = level
		self.tile_rects = []

	def render(self):
		self.tile_rects = []

		for layer in self.level.visible_layers:
			for x, y, gid in layer:
				if gid > 0:
					tile = self.level.get_tile_image_by_gid(gid)
					tile = pygame.transform.scale(tile, (64, 64))

					screen.blit(tile, (x * TILE_SIZE, y * TILE_SIZE))

					self.tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

	def collision_test(self, rect, tiles):
		hit_list = []
		for tile in tiles:
			if rect.colliderect(tile):
				hit_list.append(tile)
		return hit_list
