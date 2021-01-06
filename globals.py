import pygame

pygame.font.init()

# Global Variables
clock = pygame.time.Clock()
fps = 60
WINDOW_SIZE = (1200, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
platformList = []

# Colors
WHITE = (255, 255, 255)
LIGHT_GRAY = (170,170,170)
DARK_GRAY = (100,100,100)
BLACK = (0, 0, 0)

# Fonts
defaultFont = pygame.font.Font('fonts/retro_gaming.ttf', 48)