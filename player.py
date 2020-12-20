import pygame
import sys

from scaling import *
from globals import *
from platform import *

class Player:
	def __init__(self, player_class):
		pygame.sprite.Sprite.__init__(self)
		self.player_class = player_class

		self.width = screenPercent('x', 20)
		self.height = self.width

		self.centerX = screenPercent('x', 50, self.width)
		self.centerY = screenPercent('y', 50, self.height)

		self.offsetX = 0
		self.offsetY = 0

		self.is_jumping = True
		self.is_falling = False
		
		self.x = self.centerX + self.offsetX
		self.y = self.centerY + self.offsetY

		self.speed = 6
		self.velocity = 0

		self.leftPressed = False
		self.rightPressed = False

		self.player_class.image = pygame.transform.scale(self.player_class.image, (self.width, self.height))

	def get_event(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.velocity = -self.speed
				self.leftPressed = True
			if event.key == pygame.K_RIGHT:
				self.velocity = self.speed
				self.rightPressed = True

			if event.key == pygame.K_SPACE or event.key == ord('w'):
				self.jump()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				self.velocity = self.speed
				self.leftPressed = False
			if event.key == pygame.K_RIGHT:
				self.velocity = -self.speed
				self.rightPressed = False
		
	def update(self):
		pygame.sprite.Sprite.update(self)
		self.player_class.rect.topleft = self.x, self.y

		self.centerX = screenPercent('x', 50, self.width)
		self.centerY = screenPercent('y', 50, self.height)

		self.x = self.centerX + self.offsetX
		self.y = self.centerY + self.offsetY

		self.width = screenPercent('x', 8)
		self.height = self.width

		self.player_class.image = pygame.transform.scale(self.player_class.image, (self.width, self.height))

		if self.leftPressed == True or self.rightPressed == True:
			self.offsetX += self.velocity
			
		ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)
		for g in ground_hit_list:
			self.offsetY = 0
			self.rect.bottom = g.rect.top
			self.is_jumping = False


	def gravity(self):
		if self.is_jumping == True:
			self.offsetY += 3.2

	def jump(self):
		if self.is_jumping == False:
			self.is_falling = False
			self.is_jumping = True
		if self.is_jumping and self.is_falling == False:
			self.is_falling = True
			self.offsetY -= 33

# plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
		# for p in plat_hit_list:
		# 	self.is_jumping = False
		# 	self.offsetY

		# 	#approach from bellow
		# 	if self.rect.bottom <= p.rect.bottom:
		# 		self.rect.bottom = p.rect.top
		# 	else:
		# 		self.offsetY += 3.2