import os
import pygame

pygame.font.init()

# Global Variables
path = os.path.dirname(os.path.abspath(__file__))
clock = pygame.time.Clock()
FPS = 60
WINDOW_SIZE = (1280, 800)

# Pygame displays
screen = pygame.display.set_mode(WINDOW_SIZE)

# Colors
WHITE = (255, 255, 255)
LIGHT_GRAY = (170,170,170)
DARK_GRAY = (100,100,100)
BLACK = (0, 0, 0)

# Fonts
start_menu_title_font = pygame.font.Font(f'{path}/fonts/retro_gaming.ttf', 48)
start_menu_button_font = pygame.font.Font(f'{path}/fonts/retro_gaming.ttf', 24)
default_font = pygame.font.Font(f'{path}/fonts/retro_gaming.ttf', 16)

# Scene
SCENE = "start_menu"

# Scroll
scroll = [0, 0]

def stat_bar(x, y, scale, current_value, max_value, images_path):
	bar_empty = pygame.image.load(f'{images_path}/bar_empty.png').convert_alpha()
	bar_empty = pygame.transform.scale(bar_empty, (bar_empty.get_width() * scale, bar_empty.get_height() * scale))

	bar_percentage = pygame.image.load(f'{images_path}/bar_percentage.png').convert_alpha()
	bar_percentage = pygame.transform.scale(bar_percentage, (bar_percentage.get_width() * scale, bar_percentage.get_height() * scale))

	stat_icon = pygame.image.load(f'{images_path}/stat_icon.png').convert_alpha()
	stat_icon = pygame.transform.scale(stat_icon, (stat_icon.get_width() * scale, stat_icon.get_height() * scale))

	width = stat_icon.get_width() + bar_empty.get_width() - int(7 * scale)

	cropped_surface = screen.subsurface((x + int(7 * scale), y + (stat_icon.get_height() / 2) - (bar_percentage.get_height() / 2), bar_empty.get_width(), bar_empty.get_height()))

	percentage = (current_value / max_value) * 100
	percentage_missing = 100 - percentage
	percentage_offset = int(percentage_missing * width / 100)

	text = default_font.render(f"{int(current_value)}/{int(max_value)}", True, WHITE)

	cropped_surface.blit(bar_empty, (0, 0)) # Empty bar
	cropped_surface.blit(bar_percentage, (0 - percentage_offset, 0)) # Progress bar
	screen.blit(stat_icon, (x, y)) # Stat icon

	screen.blit(text, (x + width / 2, y + 14)) # Text
