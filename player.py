import pygame

from scaling import screenPercent

class Player(pygame.sprite.Sprite):
	def __init__(self, player_class, level):
		pygame.sprite.Sprite.__init__(self)

		self.player_class = player_class

		self.level = level

		self.image = self.player_class.idle_sprite
		self.image = pygame.transform.scale(self.image, (64, 64))

		self.rect = self.image.get_rect()

		self.width = 64
		self.height = 64

		self.x = screenPercent('x', 50)
		self.y = screenPercent('y', 10)

		self.moving_right = False
		self.moving_left = False

		self.player_y_momentum = 0
		self.air_timer = 0

		self.player_x_momentum = 0
		self.player_x_speed = 8

	def get_event(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.moving_left = True
				self.player_x_momentum = -self.player_x_speed
			if event.key == pygame.K_RIGHT:
				self.moving_right = True
				self.player_x_momentum = self.player_x_speed

			if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
				if self.air_timer < 6:
					self.player_y_momentum = -15

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				self.moving_left = False
				self.player_x_momentum = self.player_x_speed
			if event.key == pygame.K_RIGHT:
				self.moving_right = False
				self.player_x_momentum = -self.player_x_speed

	def update(self):
		pygame.sprite.Sprite.update(self)

		player_movement = [0, 0]

		if self.moving_left or self.moving_right:
			player_movement[0] += self.player_x_momentum

		player_movement[1] += self.player_y_momentum

		self.player_y_momentum += 0.6
		if self.player_y_momentum > 20:
			self.player_y_momentum = 20

		self.rect, collisions = self.move(self.rect, player_movement, self.level.tile_rects)

		if collisions['bottom']:
			self.player_y_momentum = 0
			self.air_timer = 0
		elif collisions['top']:
			self.player_y_momentum = 0
		else:
			self.air_timer += 1

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

		return rect, collision_types
