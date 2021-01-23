import os
import pygame

pygame.font.init()

# Global Variables
path = os.path.dirname(os.path.abspath(__file__))
clock = pygame.time.Clock()
FPS = 60
WINDOW_SIZE = (1200, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Colors
WHITE = (255, 255, 255)
LIGHT_GRAY = (170,170,170)
DARK_GRAY = (100,100,100)
BLACK = (0, 0, 0)

# Fonts
default_font = pygame.font.Font(f'{path}/fonts/retro_gaming.ttf', 48)
