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
		self.rect.y = 100

		self.speed = speed

		self.mob_movement = [0, 0]
		self.mob_y_momentum = 0

		self.player = player

		# self.player_coords = [player.rect.x, player.rect.y]

	def control(self, x, y):

		self.mob_movement[0] += x
		self.mob_movement[1] += y

	def attack(self):
		pass

	def follow(self):
		if self.player.rect.x > self.rect.x:
			self.mob_movement[0] = self.speed
		elif self.player.rect.x < self.rect.x:
			self.mob_movement[0] = -self.speed
		else:
			self.mob_movement[0] = 0

		# IF BOTTOM OF PLAYER <= BOTTOM OF SLIME
		# if self.player.rect.y + self.player.rect.height <= self.rect.y + self.rect.height:
			# self.mob_y_momentum = -5
		# else:
		# 	self.mob_y_momentum += 0.01
			# self.mob_movement[1] += self.mob_y_momentum

		# if self.mob_y_momentum > 1:
		# 	self.mob_y_momentum = 1



	def update(self):
		pygame.sprite.Sprite.update(self)
		self.rect.x = self.rect.x + self.mob_movement[0]
		self.rect.y = self.rect.y + self.mob_movement[1]

		if self.mob_movement[0] < 0:
			self.frame 

		


		# self.mob_y_momentum += 0.2
		# self.mob_movement[1] += self.mob_y_momentum

		# if self.mob_y_momentum >= 1:
		# 	self.mob_y_momentum = 1

		# self.rect, collisions = self.move(self.rect, self.mob_movement, self.level.tile_rects)

		# if collisions['bottom']:
		# 	self.mob_y_momentum = 0
		# elif collisions['top']:
		# 	self.mob_y_momentum = 0

		# self.follow()

		# if self.rect.colliderect(self.player.rect):
			# self.player.stats['health']['current'] -= 1

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
