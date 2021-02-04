import pygame
import pytmx
from globals import path, screen, scroll

TILE_SIZE = 64

level_1 = pytmx.load_pygame(f'{path}/level_1.tmx')

class Level:
	def __init__(self, level):
		self.level = level
		self.tile_rects = []
		self.offset = [0, 0]

	def render(self):
		self.tile_rects = []

		for layer in self.level.visible_layers:
			for x, y, gid in layer:
				if gid > 0:
					tile = self.level.get_tile_image_by_gid(gid)
					tile = pygame.transform.scale(tile, (TILE_SIZE, TILE_SIZE))

					screen.blit(tile, (x * TILE_SIZE - int(scroll[0]), y * TILE_SIZE - int(scroll[1])))

					self.tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

	def collision_test(self, rect, tiles):
		hit_list = []
		for tile in tiles:
			if rect.colliderect(tile):
				hit_list.append(tile)
		return hit_list
