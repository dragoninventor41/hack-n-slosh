import pygame
from globals import path

class Assassin:
	def __init__(self):
		self.idle_sprite = pygame.image.load(f'{path}/assets/summoner.jpg').convert() # Currently using prototype summoner image, to be changed to a spritesheet with animations later
