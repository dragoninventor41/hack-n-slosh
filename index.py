import pygame
import math
import sys
import os

pygame.init()

# Global Variables
fps = 60
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
background = pygame.Surface(screen.get_size())
clock = pygame.time.Clock()
scene = "main_menu"

screenWidth = screen.get_size()[0]
screenHeight = screen.get_size()[1]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Title
pygame.display.set_caption("Hack-n-slosh")

class Knight(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.idle_sprite = pygame.image.load('assets/smiley.png').convert()
		self.idle_sprite = pygame.transform.scale(self.idle_sprite, (50, 50))

		self.image = self.idle_sprite
		self.rect = self.image.get_rect()
		# self.rect.topleft = width/2, height/2

class Player:
	def __init__(self, player_class):
		pygame.sprite.Sprite.__init__(self)
		self.player_class = player_class

		self.width = 50
		self.height = 50

		self.pressedLeft = False
		self.pressedRight = False
		self.pressedJump = False

		self.x = (screenWidth / 2)
		self.y = (screenHeight / 2)

	def get_event(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				self.pressedRight = True
			if event.key == pygame.K_LEFT:
				self.pressedLeft = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				self.pressedRight = False
			if event.key == pygame.K_LEFT:
				self.pressedLeft = False

	def update(self):
		pygame.sprite.Sprite.update(self)
		self.player_class.rect.topleft = self.x, self.y

		if self.pressedRight == True:
			self.x += 4
		elif self.pressedLeft == True:
			self.x -= 4

		if self.pressedLeft == True:
			self.x -= 4
		elif self.pressedRight == True:
			self.x += 4

# Sets player class
player = Player(Knight())

# Game loop
while True:
	screen.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		player.get_event(event)

		if event.type == pygame.VIDEORESIZE:
			screenWidth = screen.get_size()[0]
			screenHeight = screen.get_size()[1]

	# character = Character()

	# if scene == "main_menu":

	clock.tick(fps)

	pygame.sprite.RenderPlain((player.player_class)).draw(screen)
	player.update()

	# screen.blit(background, (0, 0))

	pygame.display.flip()
