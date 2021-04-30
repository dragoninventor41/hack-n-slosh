import pygame
from globals import screen, path, SCALE
from player_classes import player_classes
from scaling import screen_percent

# Display stuff
# Get events
# Set player class

class Parchment:
	def __init__(self, player_class, x, y):
		self.x = x
		self.y = y

		self.mouse_pos = pygame.mouse.get_pos()

		self.expand_count = 0

		self.parchment_rect = pygame.Rect(x, y, 72*SCALE, (72+self.expand_count)*SCALE)

		self.parchment_surface = screen.subsurface(self.parchment_rect)

		self.parchment_image = pygame.image.load(f'{path}/assets/images/menus/class_selection/parchment.png').convert_alpha()
		self.parchment_image = pygame.transform.scale(self.parchment_image, (self.parchment_image.get_width() * SCALE, self.parchment_image.get_height() * SCALE))

		self.parchment_image_bottom = pygame.image.load(f'{path}/assets/images/menus/class_selection/parchment_bottom.png').convert_alpha()
		self.parchment_image_bottom = pygame.transform.scale(self.parchment_image_bottom, (self.parchment_image_bottom.get_width() * SCALE, self.parchment_image_bottom.get_height() * SCALE))

	def update(self):
		if self.parchment_rect.collidepoint(pygame.mouse.get_pos()):
			self.parchment_surface.blit(self.parchment_image, (0, 0))

			if self.expand_count < (108-7)*SCALE:
				self.expand_count += 12*SCALE

				self.parchment_rect.height += 12*SCALE

				self.parchment_rect.y -= 6*SCALE

		else:
			if self.expand_count > 4:
				self.expand_count -= 12*SCALE
				self.parchment_rect.height -= 12*SCALE

				self.parchment_rect.y += 6*SCALE

			self.parchment_surface.blit(self.parchment_image, (0, 0))

		self.parchment_surface = screen.subsurface(self.parchment_rect)
		self.parchment_surface.blit(self.parchment_image_bottom, (0, self.expand_count+(72-7)*SCALE))

player_class_scrolls = []

# for count, player_class in enumerate(player_classes):
	# player_class_scrolls.append(Parchment(player_class, 6*SCALE+(count*78*SCALE), screen_percent('y', 50, 72*SCALE)))

def class_selection_menu():
	for player_class_scroll in player_class_scrolls:
		player_class_scroll.update()
