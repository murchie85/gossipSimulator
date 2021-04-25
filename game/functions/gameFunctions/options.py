
import pygame
from .game_functions import *

def options(FPS,SCREEN,myfont):
	# Initialisation
	SCREEN.fill((0,0,0))
	clock = pygame.time.Clock()
	optionRun = True



	while optionRun:
		drawText(SCREEN,myfont,'menu', 100,100)

		#-- ACTIONS
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_g]:
			optionRun = False


		for event in pygame.event.get():
			if event.type == pygame.QUIT:optionRun = False

		update()
		clock.tick(FPS)


