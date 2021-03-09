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

# Background
background = pygame.Rect(0, 0, WINDOW_SIZE[0], WINDOW_SIZE[1])

# Sets level
level = Level(level_1)

# Sets player class
player = Player(Mage(), level)

# Scene Functions
def start_menu():
	screen.fill(BLACK)

	title = start_menu_title_font.render("Hack-N-Slosh", True, WHITE)
	screen.blit(title, (screenPercent('x', 50, title.get_width(), 'center'), screenPercent('y', 15, title.get_height(), 'center')))

	singleplayer_button = StartMenuButton("Singleplayer", ((screenPercent('x', 50, 400, 'center'), screenPercent('y', 50, 48, 'center')), (400, 48)), "game")
	multiplayer_button = StartMenuButton("Multiplayer", ((screenPercent('x', 50, 400, 'center'), screenPercent('y', 70, 48, 'center')), (400, 48)), "game")

	singleplayer_button.render()
	multiplayer_button.render()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		singleplayer_button.get_event(event)
		multiplayer_button.get_event(event)

def game():
	# screen.fill((200, 200, 255))

	# level.render()
	level.update()

	player.update()
	# pygame.sprite.RenderPlain((player)).draw(screen)

	# Later during optimization phase fix jittering perhaps (more noticable at lower camera speeds)
	scroll[0] += (player.rect.x - scroll[0] - (640 - 32)) / 10
	scroll[1] += (player.rect.y - scroll[1] - (400 - 32)) / 10

	# Scroll lock prevents scroll's x values from allowing view to see beyond map
	if scroll[0] <= 0:
		scroll[0] = 0
	if scroll[0] >= level.level.tilewidth * 4 * level.level.width - WINDOW_SIZE[0]:
		scroll[0] = level.level.tilewidth * 4 * level.level.width - WINDOW_SIZE[0]

	# Player x lock prevents player from falling off the sides of the map through the x value
	if player.rect.x <= 0:
		player.rect.x = 0
	if player.rect.x >= level.level.tilewidth * 4 * level.level.width - player.rect.width:
		player.rect.x = level.level.tilewidth * 4 * level.level.width - player.rect.width

	stat_bars_surface = screen.subsurface((screenPercent('x', 50, WINDOW_SIZE[0]), WINDOW_SIZE[1] - 64), (WINDOW_SIZE[0], 48))

	stat_bar(stat_bars_surface, screenPercent('x', 45, 128*4, 'right'), 0, 4, player.stats["health"]["current"], player.stats["health"]["max"], f'{path}/assets/images/stat_bars/health') # Health Bar
	stat_bar(stat_bars_surface, screenPercent('x', 55, 128*4, 'left'), 0, 4, player.stats["mana"]["current"], player.stats["mana"]["max"], f'{path}/assets/images/stat_bars/mana') # Mana Bar

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		player.get_event(event)

# Game loop
while True:
	pygame.draw.rect(screen, (200, 200, 255), (background))

	if scene_manager.scene == "start_menu":
		start_menu()
	elif scene_manager.scene == "game":
		game()
	else:
		print(f"Invalid scene:\nSCENE = {scene_manager.scene}")
		break

	clock.tick(FPS)

	pygame.display.flip()
