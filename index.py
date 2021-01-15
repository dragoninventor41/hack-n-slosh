import sys
import pygame

# from platform import Platform
from scaling import screenPercent
# from buttons import *
from player import Player
from player_classes import Assassin #, Ranger, Mage, Summoner

from globals import *

pygame.init()

# Scene
SCENE = "game"

# Title
pygame.display.set_caption("Hack-n-slosh")

# playButton = StartMenuButton("Play", ((200, 200)), "game")
def start_menu():
	# play = Button(default_font, "Play", 48, ((200, 200), (100, 40)))
	# play = Button(default_font, "Play", 48, ((200, 200)), WHITE, BLACK, on_click="game")
	# playButton.render()
	text = defaultFont.render("Hack-N-Slosh", True, WHITE)
	screen.blit(text, (screenPercent('x', 50, text.get_width()), screenPercent('y', 15, text.get_height())))

# Sets player class
player = Player(Assassin())

# Game loop
while True:
	screen.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		player.get_event(event)

		if event.type == pygame.VIDEORESIZE:
			screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
			pygame.display.set_caption(f"Hack-n-slosh {screen.get_width()}x{screen.get_height()}") # For testing purposes

	if SCENE == "start_menu":
		start_menu()
	elif SCENE == "game":
		pygame.sprite.RenderPlain((player.player_class)).draw(screen)
	else:
		print(f"Invalid scene:\nscene = {SCENE}")
		break

	clock.tick(fps)

	player.update()

	pygame.display.update()
