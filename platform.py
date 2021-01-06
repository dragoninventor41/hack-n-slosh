import os
from globals import *

"""
Possibly needs an entire rework at some point
"""

platform_list = []

# x location, y location, img width, img height, img file
class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height, img):
		pygame.sprite.Sprite.__init__(self)

		self.img = img

		print(self.img)

		if self.img != None:
			self.img = pygame.image.load(os.path.join('assets', self.img)).convert()
			self.img.convert_alpha()
			self.img.set_colorkey()

		self.rect = self.img.get_rect()
		self.rect.y = y
		self.rect.x = x

		# global platformList
		# platformList += len(platformList)
		platformList.append(pygame.Rect(200, 200, 50, 50))

		for platform in platform_list:
			print(platform)

	def render(self):
		pass