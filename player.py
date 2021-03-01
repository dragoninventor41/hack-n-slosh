import pygame
from globals import scroll, screen

class Player(): # (pygame.sprite.Sprite)
	def __init__(self, player_class, level):
		# pygame.sprite.Sprite.__init__(self)

		self.player_class = player_class

		self.level = level

		self.image = self.player_class.idle_sprite
		self.image = pygame.transform.scale(self.image, (64, 64))

		self.rect = self.image.get_rect()

		self.rect.x = 100 + scroll[0]
		self.rect.y = 100 + scroll[0]

		self.moving_right = False
		self.moving_left = False

		self.player_y_momentum = 0
		self.player_x_momentum = 0

		self.air_timer = 0

		self.max_health = 100
		self.health = self.max_health

		self.max_mana = 100
		self.mana = self.max_mana

		self.player_movement = [0, 0]

		self.player_speed = 8
		self.player_dash_speed = 18

		self.dash = False
		self.double_jump = 1000 # Normally 1, 1000 for testing purposes

	def get_event(self, event):
		if event.type == pygame.KEYDOWN:
			# Left and Right Controls
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				self.moving_left = True
				self.player_x_momentum = -self.player_speed

			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				self.moving_right = True
				self.player_x_momentum = self.player_speed

			# Double Jump
			if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
				if self.air_timer < 6:
					self.player_y_momentum = -12
				elif self.double_jump > 0:
					if self.mana >= 5:
						self.double_jump -= 1
						self.player_y_momentum = -15
						self.mana -= 5

		if event.type == pygame.KEYUP:
			# Left or Right Release
			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				self.moving_left = False
				self.player_x_momentum = self.player_speed
			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				self.moving_right = False
				self.player_x_momentum = -self.player_speed


	def update(self):
		# pygame.sprite.Sprite.update(self)
		screen.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))

		self.player_movement = [0, 0]

		if self.moving_left or self.moving_right:
			self.player_movement[0] += self.player_x_momentum

		self.player_movement[1] += self.player_y_momentum

		self.player_y_momentum += 0.6

		if self.player_y_momentum > 20:
			self.player_y_momentum = 20

		self.rect, collisions = self.move(self.rect, self.player_movement, self.level.tile_rects)

		if collisions['bottom']:
			self.player_y_momentum = 0
			self.air_timer = 0
			# self.double_jump = 0 Removed temperarily for testing purposes
		elif collisions['top']:
			self.player_y_momentum = 0
		else:
			self.air_timer += 1

		if self.mana < self.max_mana:
			self.mana += 0.04

	def move(self, rect, movement, tiles):
		collision_types = {
			'top': False,
			'bottom': False,
			'right': False,
			'left': False
		}

		rect.x += movement[0]
		hit_list = self.level.collision_test(rect, tiles)
		for tile in hit_list:
			if movement[0] > 0:
				rect.right = tile.left
				collision_types['right'] = True
			elif movement[0] < 0:
				rect.left = tile.right
				collision_types['left'] = True

		rect.y += movement[1]
		hit_list = self.level.collision_test(rect, tiles)
		for tile in hit_list:
			if movement[1] > 0:
				rect.bottom = tile.top
				collision_types['bottom'] = True
			elif movement[1] < 0:
				rect.top = tile.bottom
				collision_types['top'] = True
			else:
				rect.y += movement[1]

		return rect, collision_types
