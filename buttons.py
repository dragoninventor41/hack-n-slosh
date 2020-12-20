import pygame
from globals import *

# play = StartMenuButton("Play", ((200, 200)), "game")
class StartMenuButton:
	def __init__(self, text, coords, scene):
		self.text = defaultFont.render(text, True, WHITE)
		self.coords = coords
		self.scene = scene
		self.rect = self.text.get_size()
		self.surface = pygame.Surface(self.rect)

	def get_event(self, event):
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			self.on_hover(event)

	def on_hover(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			self.on_press()
		elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			self.on_release()

	def on_press(self):
		pass

	def on_release(self):
		global scene
		scene = self.scene

	def render(self):
		screen.blit(self.surface, self.coords)
		print(self.coords)
