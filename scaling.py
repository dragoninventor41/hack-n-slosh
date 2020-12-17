import pygame
from globals import *

def screenPercent(x_or_y, percentage, width_or_height=None, origin='center'):
	if width_or_height is None:
		if x_or_y == 'x':
			return int((screen.get_width() / 100) * percentage)
		elif x_or_y == 'y':
			return int((screen.get_height() / 100) * percentage)
		else:
			print('Invalid argument')
	else:
		if x_or_y == 'x':
			return int(((screen.get_width() / 100) * percentage) - (width_or_height / 2))
		elif x_or_y == 'y':
			return int(((screen.get_height() / 100) * percentage) - (width_or_height / 2))
		else:
			print('Invalid argument')

# screenPercent('x', 20)
