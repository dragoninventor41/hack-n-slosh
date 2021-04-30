import pygame

class Mob(pygame.sprite.Sprite):
	def __init__(self, screen, level, player, image, health, damage, speed):
		pygame.sprite.Sprite.__init__(self)

		self.level = level

		self.health = health
		self.damage = damage

		self.image = pygame.image.load(image)

		self.rect = self.image.get_rect()

		self.rect.x = 400
		self.rect.y = 20

		self.speed = speed
		self.jump = 4

		self.mob_movement = [0, 0]

		self.mob_x_momentum = 0
		self.mob_y_momentum = 0

		self.player = player

		self.air_timer = 0

		self.hostile_range = 8 # Number of tiles. Might change to pixel radius later.

		# self.player_coords = [player.rect.x, player.rect.y]

	# def control(self, x, y):
		# self.mob_movement[0] += x
		# self.mob_movement[1] += y

	def attack(self):
		pass

	def follow(self, collisions):
		if self.player.rect.x > self.rect.x:
			self.mob_x_momentum = self.speed
		elif self.player.rect.x < self.rect.x:
			self.mob_x_momentum = -self.speed
		else:
			self.mob_x_momentum = 0

		# if self.player.rect.y + self.player.rect.height - 1 < self.rect.y:
		if self.air_timer < 6:
			if collisions['left'] or collisions['right']:
				self.mob_y_momentum = -self.jump
		# else:
			# self.mob_y_momentum = 0

	def update(self):
		pygame.sprite.Sprite.update(self)

		self.mob_movement = [0, 0]

		self.mob_movement[0] += self.mob_x_momentum
		self.mob_movement[1] += self.mob_y_momentum

		self.mob_y_momentum += 0.4

		if self.mob_y_momentum > 8:
			self.mob_y_momentum = 8

		self.rect, collisions = self.move(self.rect, self.mob_movement, self.level.tile_rects)

		self.follow(collisions)

		if collisions['bottom']:
			self.mob_y_momentum = 0
			self.air_timer = 0
		elif collisions['top']:
			self.mob_y_momentum = 0
		else:
			self.air_timer += 1

		print(self.air_timer)

		# # if self.rect.colliderect(self.player.rect):
		# 	# self.player.stats['health']['current'] -= 1

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
