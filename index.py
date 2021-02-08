import sys
import pygame
from level import Level, level_1
from scaling import screenPercent
from player import Player
from player_classes import Assassin
from globals import clock, FPS, screen, default_font, WHITE, BLACK, scroll, WINDOW_SIZE

import math

pygame.init()

# Title
pygame.display.set_caption("Hack-n-slosh")

# Scene
SCENE = "game"

# Sets level
level = Level(level_1) # Could be converted to sprite / sprite collection?

# Sets player class
player = Player(Assassin(), level)

# Scene Functions
def start_menu():
	screen.fill(BLACK)
	text = default_font.render("Hack-N-Slosh", True, WHITE)
	screen.blit(text, (screenPercent('x', 50, text.get_width()), screenPercent('y', 15, text.get_height())))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

def game():
	screen.fill((200, 200, 255))

	level.render()

	player.update()
	# pygame.sprite.RenderPlain((player)).draw(screen)

	# Later during optimization phase fix jittering perhaps (more noticable at lower camera speeds)
	scroll[0] += (player.rect.x - scroll[0] - (640 - 32)) / 15
	scroll[1] += (player.rect.y - scroll[1] - (400 - 32)) / 15

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		player.get_event(event)

# Game loop
while True:
	if SCENE == "start_menu":
		start_menu()
	elif SCENE == "game":
		game()
	else:
		print(f"Invalid scene:\nscene = {SCENE}")
		break

	clock.tick(FPS)
	pygame.display.update()
