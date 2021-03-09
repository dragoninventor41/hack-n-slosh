import pygame
from globals import path

class Mage:
	def __init__(self):
		self.idle_sprite = pygame.image.load(f'{path}/assets/images/classes/mage/mage_idle.png').convert_alpha() # Currently using prototype summoner image, to be changed to a spritesheet with animations later
