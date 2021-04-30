
import pygame
from ._game_functions import *
import math

def options(FPS,SCREEN,myfont,menuFont,citizen_list,gossip_database,WIDTH,HEIGHT):
	# Initialisation
	SCREEN.fill((0,0,0))
	backgroundArray = []
	backgroundFrame = 0
	nextFrame       = pygame.time.get_ticks()
	nextSelect      = pygame.time.get_ticks()
	clock = pygame.time.Clock()
	optionRun = True
	spriteSelected = 0
	bigMenuFont = pygame.font.Font("resources/nokiafc.ttf", 24)





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
			citizenAge      = "Age             : " + str(citizen['age'])
			citizenSp       = "Status Points : " + str(citizen['SP'])
			citizenCGP      = "CGP           : " + str(citizen['CGP'])
			citizenSGP      = "SGP           : " + str(citizen['SGP'])
			citizenLocation = "Location     : " + str(citizen['location'])
			citizenRumours  = "Known Rumours : " + str(len(citizen['knownRumours']))
			citizenSprite   = citizen['sprite']

			sampleValue,sampleRumour,sampleTarget = "","",""
			if(len(citizen['knownRumours']) > 0):
				# the dict key is the key for gossip db
				sampleValue     = list(citizen['knownRumours'].keys())[0]
				sampleRumour    = str(str(gossip_database[sampleValue]['rumour']))
				sampleTarget    = str(str(gossip_database[sampleValue]['target']))
			else:
				sampleRumour    = "No Rumours"
				sampleTarget    = "No one"

			tempDict = {"citizenName": citizenName,"citizenAge": citizenAge,"citizenSp":citizenSp ,"citizenCGP":citizenCGP ,"citizenSGP":citizenSGP ,"citizenLocation": citizenLocation,"citizenRumours": citizenRumours,"citizenSprite": citizenSprite, "sampleRumour": sampleRumour, "sampleTarget":sampleTarget}
			citizenPrintArray.append(tempDict)


		# ------------TICK FRAMES

		if (gameClock > nextFrame):
			backgroundFrame = (backgroundFrame+1)%11
			nextFrame += 60



		# -------------DRAW

		draw_back(SCREEN,backgroundArray[backgroundFrame],x=0,y=0)
		drawText(SCREEN,bigMenuFont,'Rumour Insights', 0.38*WIDTH,100)



		# LEFT SIDE PRINTED TEXT
		# this pulles from an array of dicts, using spriteselected as index (this is incremented pushing left or right keys)
		drawText(SCREEN,menuFont,citizenPrintArray[spriteSelected]['citizenName'], 0.1*WIDTH,0.3*HEIGHT)
		drawText(SCREEN,menuFont,citizenPrintArray[spriteSelected]['citizenAge'], 0.1*WIDTH,0.35*HEIGHT)
		drawText(SCREEN,menuFont,citizenPrintArray[spriteSelected]['citizenLocation'], 0.1*WIDTH,0.4*HEIGHT)
		drawText(SCREEN,menuFont,citizenPrintArray[spriteSelected]['citizenSp'], 0.1*WIDTH,0.45*HEIGHT)
		drawText(SCREEN,menuFont,citizenPrintArray[spriteSelected]['citizenCGP'], 0.1*WIDTH,0.5*HEIGHT)
		drawText(SCREEN,menuFont,citizenPrintArray[spriteSelected]['citizenSGP'], 0.1*WIDTH,0.55*HEIGHT)
		drawText(SCREEN,menuFont,citizenPrintArray[spriteSelected]['citizenRumours'], 0.1*WIDTH,0.6*HEIGHT)
		
		# RIGHT SIDE PRINTED TEXT
		drawText(SCREEN,menuFont,"Sample Rumour: ", 0.5*WIDTH,0.3*HEIGHT)
		drawText(SCREEN,menuFont,str("Target: " + str(citizenPrintArray[spriteSelected]['sampleTarget'])), 0.5*WIDTH,0.40*HEIGHT)
		# write rumour, split onto two lines if needed
		selectedRumour = citizenPrintArray[spriteSelected]['sampleRumour']
		rows = math.ceil(len(selectedRumour)/40)
		startL =0
		for i in range(1,rows+1):
			rowlen = 39
			drawText(SCREEN,menuFont,str(selectedRumour)[startL:startL + rowlen ], 0.5*WIDTH,((0.40 + i*0.05)*HEIGHT))
			startL=rowlen*i

		draw_spriteScaled(SCREEN,citizenPrintArray[spriteSelected]['citizenSprite'],pygame.Rect(WIDTH/2,0.7*HEIGHT,16,16),0,"down",0,96,96)





		drawText(SCREEN,menuFont,'[B] Back', 0.8*WIDTH,0.9*HEIGHT)


		#-------------ACTIONS

		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_b]:
			optionRun = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:optionRun = False

		update()
		clock.tick(FPS)


