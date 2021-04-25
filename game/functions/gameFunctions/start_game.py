
import pygame
from .game_functions import *
from .create_citizen import *



## Initialises Citizen List





def startGame(FPS,SCREEN,myfont,citizen_list,numberOfCitizens,CITIENSCREATED='no',timer=0):
	# Initialisation
	clock = pygame.time.Clock()
	optionRun = True


	while optionRun:
		keys_pressed = pygame.key.get_pressed()
		SCREEN.fill((0,0,0))
		drawText(SCREEN,myfont,'Welcome To Celestus', 0.45*WIDTH, 0.1*HEIGHT)
		
		if(len(citizen_list) <1):
			drawText(SCREEN,myfont,'Generating Citiens',0.45*WIDTH, 0.5*HEIGHT)
			citizen_list = generateCitizens(numberOfCitizens)
		
		## Display message for certain time 
		if((CITIENSCREATED == "no") and (len(citizen_list) >1)):
			timer+=1
			drawText(SCREEN,myfont,'Citiens Created',0.45*WIDTH, 0.45*HEIGHT)
			if(timer>30): CITIENSCREATED = "yes"


			
			


		#-- ACTIONS
		if keys_pressed[pygame.K_g]:
			optionRun = False
			


		for event in pygame.event.get():
			if event.type == pygame.QUIT:optionRun = False

		update()
		clock.tick(FPS)

	return(citizen_list)

