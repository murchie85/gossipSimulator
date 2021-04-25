
import pygame
from .game_functions import *

def options(FPS,SCREEN,myfont,menuFont,citizen_list):
	# Initialisation
	SCREEN.fill((0,0,0))
	backgroundArray = []
	backgroundFrame = 0
	nextFrame       = pygame.time.get_ticks()
	clock = pygame.time.Clock()
	optionRun = True



	# -----------Append all background images

	for i in range(1,12):
		backPath = "/Users/adammcmurchie/2021/fishwives/sprites/menu/blackblue" + str(i) + ".png"
		back   = pygame.image.load(backPath)
		back   = pygame.transform.scale(back, (WIDTH, HEIGHT))
		backgroundArray.append(back)



	# ----------------MAIN LOOP

	while optionRun:
		gameClock   = pygame.time.get_ticks()

		for key in citizen_list:
			citizen = citizen_list[key]
			

		# ------------TICK FRAMES

		if (gameClock > nextFrame):
			backgroundFrame = (backgroundFrame+1)%11
			nextFrame += 60



		# -------------DRAW

		draw_back(SCREEN,backgroundArray[backgroundFrame],x=0,y=0)
		drawText(SCREEN,myfont,'menu', 100,100)
		drawText(SCREEN,menuFont,'[B] Back', 0.8*WIDTH,0.9*HEIGHT)


		#-------------ACTIONS

		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_b]:
			optionRun = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:optionRun = False

		update()
		clock.tick(FPS)


