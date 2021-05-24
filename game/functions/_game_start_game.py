
import pygame
from ._game_functions import *
from ._game_draw import *
from .processCitizen import *
import csv



## Initialises Citizen List





def startGame(FPS,SCREEN,myfont,citizen_list,numberOfCitizens, WIDTH,HEIGHT,LOGFILE,CITIENSCREATED='no',timer=0):
	# Initialisation
	clock = pygame.time.Clock()
	optionRun = True
	nextFrame       = pygame.time.get_ticks()
	nextSelect      = pygame.time.get_ticks()
	backgroundArray = []
	backgroundFrame = 0


	# INITIALISE LOG FILE 

	with open(LOGFILE, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['Time','ID','Spreader','Audience','SP','Originalsp','AudienceKnownRumours','rumour target','sentiment','TotalRumours'])





	# -----------Append all background images

	for i in range(1,14):
		backPath = "/Users/adammcmurchie/2021/Celestus/sprites/Title/title" + str(i) + ".png"
		back   = pygame.image.load(backPath)
		back   = pygame.transform.scale(back, (WIDTH, HEIGHT))
		backgroundArray.append(back)




	while optionRun:
		gameClock   = pygame.time.get_ticks()
		keys_pressed = pygame.key.get_pressed()
		SCREEN.fill((0,0,0))
		drawText(SCREEN,myfont,'Welcome To Celestus', 0.42*WIDTH, 0.1*HEIGHT)
		
		if(len(citizen_list) <1):
			drawText(SCREEN,myfont,'Generating Citiens',0.45*WIDTH, 0.5*HEIGHT)
			citizen_list = generateCitizens(numberOfCitizens)
		

		# ------------TICK FRAMES

		if (gameClock > nextFrame):
			backgroundFrame = (backgroundFrame+1)%11
			nextFrame += 120



		# -------------DRAW

		draw_back(SCREEN,backgroundArray[backgroundFrame],x=0,y=0)

		## Display message for certain time 
		if((CITIENSCREATED == "no") and (len(citizen_list) >1)):
			timer+=1
			drawText(SCREEN,myfont,'Citiens Created',0.45*WIDTH, 0.45*HEIGHT)
			if(timer>30): CITIENSCREATED = "yes"


		if(CITIENSCREATED == "yes"):
			drawText(SCREEN,myfont,'Press G to Start', 0.42*WIDTH, 0.7*HEIGHT)
			
			


		#-- ACTIONS
		if keys_pressed[pygame.K_g] or keys_pressed[pygame.K_RETURN]:
			optionRun = False
			


		for event in pygame.event.get():
			if event.type == pygame.QUIT:optionRun = False

		update()
		clock.tick(FPS)

	return(citizen_list)

