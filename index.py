import sys
import pygame
from level import Level, level_1
from scaling import screen_percent
from player import Player
from player_classes import Mage
from globals import clock, FPS, screen, WHITE, BLACK, scroll, stat_bar, path, start_menu_title_font, scene_manager, WINDOW_SIZE
from button import StartMenuButton
from menus import class_selection_menu
from mob import Mob
import pyscroll
import pytmx

pygame.init()

# Title
pygame.display.set_caption("Hack-n-slosh")

# Background
background = pygame.Rect(0, 0, WINDOW_SIZE[0], WINDOW_SIZE[1])

# Sets player class
level = Level(level_1)
# level = pytmx.load_pygame(f'{path}/level_1.tmx')
player = Player(Mage(), level)

# Sets level
map_data = pyscroll.TiledMapData(pytmx.load_pygame(f'{path}/level_1.tmx'))
map_layer = pyscroll.BufferedRenderer(map_data, WINDOW_SIZE)

group = pyscroll.PyscrollGroup(map_layer=map_layer)
group.add(player)

player.rect.center = 200, 200

group.center(player.rect.center)

map_layer.zoom = 4.0

# Slime
slime = Mob(level, player, f'{path}/assets/images/mobs/slime.png', 20, 5, 4)

# Scene Functions
def start_menu():
	screen.fill(BLACK)

	title = start_menu_title_font.render("Hack-N-Slosh", True, WHITE)
	class_selection_menu()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


def game():
	# level.update()

	# player.update()

	group.center(player.rect.center)

	group.draw(screen)
	player.update()

	# slime.update()

	# scroll[0] += (player.rect.x - scroll[0] - (640 - 32)) / 10
	# scroll[1] += (player.rect.y - scroll[1] - (400 - 32)) / 10

	# Scroll lock prevents scroll's x values from allowing view to see beyond map
	# if scroll[0] <= 0:
		# scroll[0] = 0
	# if scroll[0] >= level.level.tilewidth * 4 * level.level.width - WINDOW_SIZE[0]:
		# scroll[0] = level.level.tilewidth * 4 * level.level.width - WINDOW_SIZE[0]

	# Player x lock prevents player from falling off the sides of the map through the x value
	# if player.rect.x <= 0:
		# player.rect.x = 0
	# if player.rect.x >= level.level.tilewidth * 4 * level.level.width - player.rect.width:
		# player.rect.x = level.level.tilewidth * 4 * level.level.width - player.rect.width

	# stat_bars_surface = screen.subsurface((screen_percent('x', 50, WINDOW_SIZE[0]), WINDOW_SIZE[1] - 64), (WINDOW_SIZE[0], 48))

	# stat_bar(stat_bars_surface, screen_percent('x', 45, 128*4, 'right'), 0, 4, player.stats["health"]["current"], player.stats["health"]["max"], f'{path}/assets/images/stat_bars/health') # Health Bar
	# stat_bar(stat_bars_surface, screen_percent('x', 55, 128*4, 'left'), 0, 4, player.stats["mana"]["current"], player.stats["mana"]["max"], f'{path}/assets/images/stat_bars/mana') # Mana Bar

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
