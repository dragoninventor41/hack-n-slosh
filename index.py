import sys
import pygame
from player import Player
from player_classes import Assassin, Ranger, Mage, Summoner
from mobs import Mob
import pyscroll
import pytmx
import os

pygame.init()

# Title
pygame.display.set_caption("Hack-n-slosh")

class Game():
	def __init__(self):
		# Main Variables
		self.path = os.path.dirname(os.path.abspath(__file__))
		self.clock = pygame.time.Clock()
		self.fps = 60
		self.window_size = (1920, 1080)
		self.screen = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)
		self.scale = 4
		self.fonts = {
			"default": pygame.font.Font(f'{self.path}/fonts/retro_gaming.ttf', 16),
			"start_menu_title": pygame.font.Font(f'{self.path}/fonts/retro_gaming.ttf', 48),
			"start_menu_button": pygame.font.Font(f'{self.path}/fonts/retro_gaming.ttf', 24)
		}

		# Level
		self.level = {
			"level": 1
		}

		try:
			self.level["tmx"] = pytmx.load_pygame(f'{self.path}/worlds/techno/levels/{self.level["level"]}.tmx')
		except:
			print(f'Level {self.level["level"]} does not exist.')
			sys.exit()

		self.level["map_layer"] = pyscroll.BufferedRenderer(pyscroll.TiledMapData(self.level["tmx"]), self.window_size)
		
		self.level["TILE_SIZE"] = 16
		self.level["tile_rects"] = []
		for layer in self.level["tmx"].visible_layers:
			for tile_x, tile_y, gid in layer:
				if gid > 0:
					self.level["tile_rects"].append(pygame.Rect(tile_x * self.level["TILE_SIZE"], tile_y * self.level["TILE_SIZE"], self.level["TILE_SIZE"], self.level["TILE_SIZE"]))

		# Player
		self.player = Player(Mage(), self.level["tile_rects"], self.tile_collision_test, self.screen)
		self.player.rect.center = 400, 400

		# Slime
		# self.slime = Mob(self.screen, self.level_tile_rects, self.player, f'{self.path}/worlds/techno/mobs/slime/slime.png', 40, 0.5, 2)

		# Group
		self.group = pyscroll.PyscrollGroup(map_layer=self.level["map_layer"])

		# self.group.add(self.slime)
		self.group.add(self.player)

		self.group.center(self.player.rect.center)

		self.level["map_layer"].zoom = 4.0

	def tile_collision_test(self, rect, tiles):
		hit_list = []
		for tile in tiles:
			if rect.colliderect(tile):
				hit_list.append(tile)
		return hit_list

	def draw(self):
		self.group.center(self.player.rect.center)
		self.group.draw(self.screen)

	def get_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			self.player.get_event(event)

	def update(self):
		self.group.update()

	def run(self):
		self.clock = pygame.time.Clock()

		self.get_events()
		self.update()
		self.draw()

game = Game()
# Game loop
while True:
	game.run()
	game.clock.tick(game.fps)
	pygame.display.flip()

