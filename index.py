import sys
import pygame
from level import Level, level_1
from scaling import screenPercent
from player import Player
from player_classes import Mage
from globals import clock, FPS, screen, WHITE, BLACK, scroll, stat_bar, path, start_menu_title_font, scene_manager, WINDOW_SIZE
from button import StartMenuButton


pygame.init()

# Title
pygame.display.set_caption("Hack-n-slosh")

# Sets level
level = Level(level_1)

# Sets player class
player = Player(Mage(), level)

# Scene Functions
def start_menu():
	screen.fill(BLACK)

	title = start_menu_title_font.render("Hack-N-Slosh", True, WHITE)
	screen.blit(title, (screenPercent('x', 50, title.get_width()), screenPercent('y', 15, title.get_height())))

	singleplayer_button = StartMenuButton("Singleplayer", ((screenPercent('x', 50, 400), screenPercent('y', 50)), (400, 48)), "game")
	multiplayer_button = StartMenuButton("Multiplayer", ((screenPercent('x', 50, 400), screenPercent('y', 70)), (400, 48)), "game")

	singleplayer_button.render()
	multiplayer_button.render()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		singleplayer_button.get_event(event)
		multiplayer_button.get_event(event)

def game():
	screen.fill((200, 200, 255))

	# level.render()
	level.update()

	player.update()
	# pygame.sprite.RenderPlain((player)).draw(screen)

	# Later during optimization phase fix jittering perhaps (more noticable at lower camera speeds)
	scroll[0] += (player.rect.x - scroll[0] - (640 - 32)) / 15
	scroll[1] += (player.rect.y - scroll[1] - (400 - 32)) / 15

	stat_bars_surface = screen.subsurface((screenPercent('x', 50, WINDOW_SIZE[0]), WINDOW_SIZE[1] - 48), (WINDOW_SIZE[0], 48))

	stat_bar(stat_bars_surface, screenPercent('x', 25), 0, 4, player.health, player.max_health, f'{path}/assets/stat_bar/health') # Health Bar
	stat_bar(stat_bars_surface, screenPercent('x', 50), 0, 4, player.mana, player.max_mana, f'{path}/assets/stat_bar/mana') # Mana Bar

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		player.get_event(event)

# Game loop
while True:
	if scene_manager.scene == "start_menu":
		start_menu()
	# if SCENE == "start_menu_singleplayer":
	# 	start_menu().start_menu_singleplayer()
	elif scene_manager.scene == "game":
		game()
	else:
		print(f"Invalid scene:\nSCENE = {SCENE}")
		break

	clock.tick(FPS)
	# print(f'FPS: {int(clock.get_fps())}')

	pygame.display.update()
