import pygame

pygame.font.init()

# Global Variables
clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
platformList = []

# Colors
WHITE = (255, 255, 255)
LIGHT_GRAY = (170,170,170)
DARK_GRAY = (100,100,100)
BLACK = (0, 0, 0)

# Fonts
defaultFont = pygame.font.Font('fonts/retro_gaming.ttf', 48)