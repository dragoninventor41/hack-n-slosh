import pygame
import pytmx
from globals import path, screen, scroll

TILE_SIZE = 16
CHUNK_SIZE = 8

game_map = {}

level_1 = pytmx.load_pygame(f'{path}/level_1.tmx')

class Level:
	def __init__(self, level):
		self.level = level
		self.tile_rects = []
		self.chunk_data = []

		for layer in self.level.visible_layers:
			for tile_x, tile_y, gid in layer:
				self.chunk_data = []
				if gid > 0:
					self.tile_rects.append(pygame.Rect(tile_x * TILE_SIZE, tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))


	# def update(self):
		# for layer in self.level.visible_layers:
			# for x, y, gid in layer:
				# if gid > 0:
					# tile = self.level.get_tile_image_by_gid(gid).convert()
					# tile = pygame.transform.scale(tile, (TILE_SIZE, TILE_SIZE))

					# screen.blit(tile, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))

	def collision_test(self, rect, tiles):
		hit_list = []
		for tile in tiles:
			if rect.colliderect(tile):
				hit_list.append(tile)
		return hit_list
