from platform import level_1, Level
import sys
import pygame

from scaling import screenPercent
from player import Player
from player_classes import Assassin

from globals import clock, FPS, screen, default_font, WHITE, BLACK

pygame.init()

# Scene
SCENE = "game"

# Title
pygame.display.set_caption("Hack-n-slosh")

# Scene Functions
def start_menu():
	text = default_font.render("Hack-N-Slosh", True, WHITE)
	screen.blit(text, (screenPercent('x', 50, text.get_width()), screenPercent('y', 15, text.get_height())))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

def game():
	level.render()
	pygame.sprite.RenderPlain((player)).draw(screen)
	player.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		player.get_event(event)

# Sets level
level = Level(level_1) # Could be converted to sprite / sprite collection?

# Sets player class
player = Player(Assassin(), level)

# Game loop
while True:
	screen.fill(BLACK)

	if SCENE == "start_menu":
		start_menu()
	elif SCENE == "game":
		game()
	else:
		print(f"Invalid scene:\nscene = {SCENE}")
		break

	clock.tick(FPS)
	pygame.display.update()
