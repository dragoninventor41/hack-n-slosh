import pygame
from globals import path

class Assassin:
	def __init__(self):
		self.idle_sprite = pygame.image.load(f'{path}/player_classes/mage/mage_idle.png').convert_alpha() # Currently using prototype summoner image, to be changed to a spritesheet with animations later

		self.description = "Is mage, mage do mage ting"

class Ranger:
	def __init__(self):
		self.idle_sprite = pygame.image.load(f'{path}/player_classes/mage/mage_idle.png').convert_alpha() # Currently using prototype summoner image, to be changed to a spritesheet with animations later

		self.description = "Is mage, mage do mage ting"

class Mage:
	def __init__(self):
		self.idle_sprite = pygame.image.load(f'{path}/player_classes/mage/mage_idle.png').convert_alpha() # Currently using prototype summoner image, to be changed to a spritesheet with animations later

		self.description = "Is mage, mage do mage ting"

class Summoner:
	def __init__(self):
		self.idle_sprite = pygame.image.load(f'{path}/player_classes/mage_idle.png').convert_alpha() # Currently using prototype summoner image, to be changed to a spritesheet with animations later

		self.description = "Is mage, mage do mage ting"

player_classes = [Assassin, Ranger, Mage, Summoner]
