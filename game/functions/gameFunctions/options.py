
import pygame
from .game_functions import *

def options(FPS,SCREEN,myfont,menuFont,citizen_list):
	# Initialisation
	SCREEN.fill((0,0,0))
	backgroundArray = []
	backgroundFrame = 0
	nextFrame       = pygame.time.get_ticks()
	nextSelect      = pygame.time.get_ticks()
	clock = pygame.time.Clock()
	optionRun = True
	spriteSelected = 0





	# -----------Append all background images

	for i in range(1,12):
		backPath = "/Users/adammcmurchie/2021/fishwives/sprites/menu/blackblue" + str(i) + ".png"
		back   = pygame.image.load(backPath)
		back   = pygame.transform.scale(back, (WIDTH, HEIGHT))
		backgroundArray.append(back)



	# ----------------MAIN LOOP

	while optionRun:
		gameClock   = pygame.time.get_ticks()
		citizenPrintArray = []
		
		keys_pressed = pygame.key.get_pressed()
		# INCREMENT CHARACTER SELECTOR 
		if (gameClock > nextSelect):
			if (keys_pressed[pygame.K_RIGHT]): spriteSelected +=1
			if (keys_pressed[pygame.K_LEFT]): spriteSelected -=1
			nextSelect += 200

		if(spriteSelected > len(citizen_list) - 1): spriteSelected=0
		if(spriteSelected < 0): spriteSelected=len(citizen_list) - 1


		for key in citizen_list:
			citizen = citizen_list[key]
			citizenName     = "Name          : " + str(citizen['name'])
			citizenAge      = "Age           : " + str(citizen['age'])
			citizenLocation = "Location      : " + str(citizen['location'])
			citizenRumours  = "Known Rumours : " + str(len(citizen['knownRumours']))
			citizenSprite   = citizen['sprite']

			tempDict = {"citizenName": citizenName,"citizenAge": citizenAge,"citizenLocation": citizenLocation,"citizenRumours": citizenRumours,"citizenSprite": citizenSprite}
			citizenPrintArray.append(tempDict)


		# ------------TICK FRAMES

		if (gameClock > nextFrame):
			backgroundFrame = (backgroundFrame+1)%11
			nextFrame += 60



		# -------------DRAW

		draw_back(SCREEN,backgroundArray[backgroundFrame],x=0,y=0)
		drawText(SCREEN,menuFont,'menu', 0.5*WIDTH,100)


		# this pulles from an array of dicts, using spriteselected as index (this is incremented pushing left or right keys)
		drawText(SCREEN,menuFont,citizenPrintArray[spriteSelected]['citizenName'], 0.1*WIDTH,0.2*HEIGHT)
		drawText(SCREEN,menuFont,citizenPrintArray[spriteSelected]['citizenAge'], 0.1*WIDTH,0.25*HEIGHT)
		drawText(SCREEN,menuFont,citizenPrintArray[spriteSelected]['citizenLocation'], 0.1*WIDTH,0.3*HEIGHT)
		drawText(SCREEN,menuFont,citizenPrintArray[spriteSelected]['citizenRumours'], 0.1*WIDTH,0.35*HEIGHT)
		
		draw_sprite(SCREEN,citizenPrintArray[spriteSelected]['citizenSprite'],pygame.Rect(WIDTH/2,0.8*HEIGHT,16,16),0,"down",0)





		drawText(SCREEN,menuFont,'[B] Back', 0.8*WIDTH,0.9*HEIGHT)


		#-------------ACTIONS

		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_b]:
			optionRun = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:optionRun = False

		update()
		clock.tick(FPS)


