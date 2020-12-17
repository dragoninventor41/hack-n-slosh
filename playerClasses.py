import pygame
from globals import *

class Necromancer(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.idle_sprite = pygame.image.load('assets/necromancer.jpg').convert()
		self.idle_sprite_scaled = pygame.transform.scale(self.idle_sprite, (self.idle_sprite.get_width(), self.idle_sprite.get_height()))

		self.image = self.idle_sprite
		self.rect = self.image.get_rect()
