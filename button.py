import pygame
from globals import start_menu_button_font, WHITE, screen, scene_manager

class StartMenuButton:
	def __init__(self, button_name, rect, on_click_scene):
		self.button_name = button_name
		self.rect = pygame.Rect(rect)
		self.on_click_scene = on_click_scene

	def render(self):
		display_name = start_menu_button_font.render(self.button_name, True, WHITE)

		pygame.draw.rect(screen, (20, 20, 20), self.rect)
		screen.blit(display_name, (self.rect.x + display_name.get_width()/2, self.rect.y))

	def get_event(self, event):
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()

			if self.rect.collidepoint(pos):
				scene_manager.change_scene('game')
