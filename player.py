import pygame

from scaling import screenPercent
from globals import *
from platform import *
from player_classes import *

test_rect = pygame.Rect(100, 550, 50, 50)

class Player:
	def __init__(self, player_class):
		pygame.sprite.Sprite.__init__(self)
		self.player_class = player_class

		self.width = 80
		self.height = 80

		# self.offset_x = 0
		# self.offset_y = 0

		self.x = screenPercent('x', 50)
		self.y = screenPercent('y', 50)

		self.is_jumping = False
		self.is_falling = False

		self.speed = 6
		# self.jump_speed = 4

		self.velocity = [0, 0] # x, y

		self.left_pressed = False
		self.right_pressed = False

		self.player_class.image = pygame.transform.scale(self.player_class.image, (self.width, self.height))

		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

	def get_event(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.velocity[0] = -self.speed
				self.left_pressed = True
			if event.key == pygame.K_RIGHT:
				self.velocity[0] = self.speed
				self.right_pressed = True

			# if event.key == pygame.K_SPACE or event.key == ord('w') or event.key == pygame.K_UP:
			# 	self.jump()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				self.velocity[0] = self.speed
				self.left_pressed = False
			if event.key == pygame.K_RIGHT:
				self.velocity[0] = -self.speed
				self.right_pressed = False

	def update(self):
		pygame.sprite.Sprite.update(self)
		self.player_class.rect.topleft = self.x, self.y

		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

		# Updates
		if self.left_pressed or self.right_pressed:
			self.x += self.velocity[0]
		self.y += self.velocity[1]


		# Detects collision against ground
		if self.y > WINDOW_SIZE[1] - self.player_class.image.get_height():
			self.velocity[1] = -self.velocity[1]
		else:
			self.velocity[1] += 0.2

		# Detects if test rect is collided
		if self.rect.colliderect(test_rect):
			pygame.draw.rect(screen, (255, 0, 0), test_rect)
		else:
			pygame.draw.rect(screen, (255, 255, 255), test_rect)
