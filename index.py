import pygame
import math

pygame.init()

# Global Variables
fps = 60
screen = pygame.display.set_mode((800, 800))
background = pygame.Surface(screen.get_size())

# Colors
WHITE = (255, 255, 255)

# Initialization
pygame.display.set_caption('Hack-n-slosh')
background = background.convert()
background.fill(WHITE)
