from globals import *

# x location, y location, img width, img height, img file
class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height, img):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join('images', img)).convert()
		self.image.convert_alpha()
		self.image.set_colorkey(ALPHA)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x

	def render(self):
		