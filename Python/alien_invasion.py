import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
	pygame.init()
	stn = Settings()
	screen=pygame.display.set_mode((stn.width,stn.height))
	pygame.display.set_caption('Alien Invasion')
	bg_color = stn.bg_color
	ship = Ship(screen, stn)
	
	#create group for keeping bullets
	bullets = Group()
	while True:
		gf.check_events(ship, stn, screen, bullets)
		ship.update()
		gf.update_bullets(bullets)	
		gf.update_screen(stn, screen, ship, bullets)
					
run_game()
