import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import gme_functions as gf

def run_game():
	#Initialize game and create a screen object.
	pygame.init()
	game_settings = Settings()
	screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
	pygame.display.set_caption('Alien Invasion Game')
	
	#Make a ship, a group of bullets, and a group of aliens.
	ship = Ship(game_settings, screen)
	bullets = Group()
	aliens = Group()
	
	#Create a fleet of aliens.
	gf.create_fleet(game_settings, screen, ship, aliens)
	
	#Setting the background colour. 
	bg_colour = game_settings.bg_colour
	
	#Start the main loop for the game. 
	active = True
	while active:
		
		#We track keyboard and mouse events.
		gf.check_events(game_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(game_settings, screen, ship, aliens, bullets)
		

run_game()
