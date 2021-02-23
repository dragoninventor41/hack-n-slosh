import sys
import pygame
from level import Level, level_1
from scaling import screenPercent
from player import Player
from player_classes import Assassin
from globals import clock, FPS, screen, default_font, WHITE, BLACK, scroll, stat_bar, path

pygame.init()

# Title
pygame.display.set_caption("Hack-n-slosh")

# Scene
SCENE = "game"

# Sets level
level = Level(level_1)

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

	# level.render()
	level.update()

	player.update()
	# pygame.sprite.RenderPlain((player)).draw(screen)

	# Later during optimization phase fix jittering perhaps (more noticable at lower camera speeds)
	scroll[0] += (player.rect.x - scroll[0] - (640 - 32)) / 15
	scroll[1] += (player.rect.y - scroll[1] - (400 - 32)) / 15

	stat_bar(20, 20, 4, player.health, player.max_health, f'{path}/assets/stat_bar/health') # Health Bar
	stat_bar(20, 72, 4, player.mana, player.max_mana, f'{path}/assets/stat_bar/mana') # Mana Bar

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
	# print(f'FPS: {int(clock.get_fps())}')

	pygame.display.update()
