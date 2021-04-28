import sys
import pygame
from level import Level, level_1
from player import Player
from player_classes import Mage
from mob import Mob
import pyscroll
import pytmx
import os

pygame.init()

# Title
pygame.display.set_caption("Hack-n-slosh")

class Game():
	def __init__(self):
		self.path = os.path.dirname(os.path.abspath(__file__))
		self.clock = pygame.time.Clock()
		self.fps = 60
		self.window_size = (1920, 1080)
		self.scale = 4

		self.screen = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)

		self.level = Level()

		self.player = Player(Mage(), self.level, self.screen)

		# TEMP
		self.slime = Mob(self.screen, self.level, self.player, f'{self.path}/assets/images/mobs/slime.png', 40, 0.5, 0.1)

		map_data = pyscroll.TiledMapData(pytmx.load_pygame(f'{self.path}/level_1.tmx'))
		map_layer = pyscroll.BufferedRenderer(map_data, self.window_size)

		self.group = pyscroll.PyscrollGroup(map_layer=map_layer)
		self.group.add(self.slime)
		self.group.add(self.player)

		self.player.rect.center = 200, 200

		self.group.center(self.player.rect.center)

		map_layer.zoom = 4.0

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
	print(game.clock.get_fps())
