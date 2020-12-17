import pygame

class Button:
	def __init__(self, font, text, fontSize, rect, txt_color, bkgr_color, on_click):
		self.font = font
		self.txt_color = txt_color
		self.text = self.font.render(self.text, True, self.txt_color) # What the actual fk was I doing here...
		self.rect = pygame.Rect(rect)
		self.bkgr_color = bkgr_color

	def render(self):
		pass

# class StartMenuButton:
	# def __init__(self):
