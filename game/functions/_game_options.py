
import pygame
from ._game_functions import *
from .rules import *
import math

def menu(FPS,SCREEN,myfont,menuFont,citizen_list,gossip_database,WIDTH,HEIGHT,imageDict):
	# Initialisation
	backgroundArray = []
	backgroundFrame = 0
	nextFrame       = pygame.time.get_ticks()
	nextSelect      = pygame.time.get_ticks()
	clock           = pygame.time.Clock()
	menuRun         = True
	menuSelected    = 0
	bigMenuFont     = pygame.font.Font("resources/nokiafc.ttf", 24)
	menuOptionsImgs = imageDict['mOptionArray']



	# -----------Append all background images

	for i in range(1,12):
		backPath = "/Users/adammcmurchie/2021/fishwives/sprites/menu/blackblue" + str(i) + ".png"
		back   = pygame.image.load(backPath)
		back   = pygame.transform.scale(back, (WIDTH, HEIGHT))
		backgroundArray.append(back)

	# ----------------MAIN LOOP

	while menuRun:
		gameClock   = pygame.time.get_ticks()
		citizenPrintArray = []	

		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_r]: rulesOptions(FPS,SCREEN,myfont,menuFont,citizen_list,gossip_database,WIDTH,HEIGHT,imageDict)
		# INCREMENT CHARACTER SELECTOR 

		# Get input without spamming
		events = pygame.event.get()
		for event in events:
		    if event.type == pygame.KEYDOWN:
		        if event.key == pygame.K_DOWN:
		            menuSelected +=1
		        if event.key == pygame.K_UP:
		            menuSelected -=1
		        if event.key == pygame.K_b:
		        	menuRun = False
			



		if(menuSelected > len(imageDict['mOptionArray']) - 1): menuSelected=0
		if(menuSelected < 0): menuSelected=len(imageDict['mOptionArray']) - 1

		if keys_pressed[pygame.K_RETURN]:
			if(menuSelected==0):
				characters(FPS,SCREEN,myfont,menuFont,citizen_list,gossip_database,WIDTH,HEIGHT,imageDict)
			if(menuSelected==2):
				rulesOptions(FPS,SCREEN,myfont,menuFont,citizen_list,gossip_database,WIDTH,HEIGHT,imageDict)
			if(menuSelected==4):
				menuRun = False


		# ------------TICK FRAMES

		if (gameClock > nextFrame):
			backgroundFrame = (backgroundFrame+1)%11
			nextFrame += 60


		# -------------DRAW

		draw_back(SCREEN,backgroundArray[backgroundFrame],x=0,y=0)
		draw_back(SCREEN,imageDict['mOptionArray'][menuSelected],x=0,y=0)

		drawText(SCREEN,bigMenuFont,'Celestus: Menu', 0.10*WIDTH,50)




		update()
		clock.tick(FPS)






def characters(FPS,SCREEN,myfont,menuFont,citizen_list,gossip_database,WIDTH,HEIGHT,imageDict):
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
		if keys_pressed[pygame.K_r]: rulesOptions(FPS,SCREEN,myfont,menuFont,citizen_list,gossip_database,WIDTH,HEIGHT,imageDict)
		# INCREMENT CHARACTER SELECTOR 

		# Get input without spamming
		events = pygame.event.get()
		for event in events:
		    if event.type == pygame.KEYDOWN:
		        if event.key == pygame.K_LEFT:
		            spriteSelected -=1
		        if event.key == pygame.K_RIGHT:
		            spriteSelected +=1
		        if event.key == pygame.K_b:
		            optionRun = False


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

		# ARROW 
		draw_back(SCREEN,imageDict['arrowLeft'],x=40,y=HEIGHT/3)
		draw_back(SCREEN,imageDict['arrowRight'],x=WIDTH - 40,y=HEIGHT/3)

		rowLen,maxRL,words,i = 0,38,"",0
		if(len(selectedRumour) <= maxRL):
			drawText(SCREEN,menuFont,str(selectedRumour),0.5*WIDTH, 0.50*HEIGHT)
		else:
			for word in selectedRumour.split():
				words+= word + ' '
				if(len(words) >= maxRL):
					drawText(SCREEN,menuFont,str(words),0.5*WIDTH, (0.50 + (i * 0.05) )*HEIGHT)
					words = ""
					i+=1
			if(words!=""): drawText(SCREEN,menuFont,str(words),0.5*WIDTH,(0.50 + (i * 0.05) )*HEIGHT)







		draw_spriteScaled(SCREEN,citizenPrintArray[spriteSelected]['citizenSprite'],pygame.Rect(WIDTH/2,0.7*HEIGHT,16,16),0,"down",0,96,96)

		drawText(SCREEN,menuFont,'[B] Back', 0.8*WIDTH,0.9*HEIGHT)
		drawText(SCREEN,menuFont,'[R] Rules', 0.7*WIDTH,0.9*HEIGHT)



		update()
		clock.tick(FPS)



def rulesOptions(FPS,SCREEN,myfont,menuFont,citizen_list,gossip_database,WIDTH,HEIGHT,imageDict):

	SCREEN.fill((0,0,0))
	backgroundArray = []
	backgroundFrame = 0
	nextFrame       = pygame.time.get_ticks()
	nextSelect      = pygame.time.get_ticks()
	clock           = pygame.time.Clock()
	rulesOptions    = True
	ruleSelected    = 0
	valueSelected   = 0 
	ruleConfirmed   = False
	bigMenuFont     = pygame.font.Font("resources/nokiafc.ttf", 24)





	# -----------Append all background images

	for i in range(1,12):
		backPath = "/Users/adammcmurchie/2021/fishwives/sprites/advancedOptions/blackblue" + str(i) + ".png"
		back   = pygame.image.load(backPath)
		back   = pygame.transform.scale(back, (WIDTH, HEIGHT))
		backgroundArray.append(back)



	# ----------------MAIN LOOP

	while rulesOptions:
		gameClock   = pygame.time.get_ticks()
		citizenPrintArray = []

		# GET RULES FROM FILE 
		rulesFile = "rules/RULES.txt"
		gossipStimulation = getFullRules(rulesFile,'gossipStimulation')
		talkingDistance   = getFullRules(rulesFile, 'talkingDistance')
		luckyChance       = getFullRules(rulesFile,'luckyChance')
		citizenWalkSpeed  = getFullRules(rulesFile,'citizenWalkSpeed')
		rulesArray = [gossipStimulation,talkingDistance,luckyChance,citizenWalkSpeed]
		ruleDescFile = "rules/rules_schema.txt"
		rulesDesc  = [str(getRulesSchema(ruleDescFile,'gossipStimulation')),
					  str(getRulesSchema(ruleDescFile,'talkingDistance')),
					  str(getRulesSchema(ruleDescFile,'luckyChance')),
					  str(getRulesSchema(ruleDescFile,'citizenWalkSpeed'))]


		chosenRule = str(rulesArray[ruleSelected].split(':')[0])
		ruleValue  = str(rulesArray[ruleSelected].split(':')[1])

		keys_pressed = pygame.key.get_pressed()
		# INCREMENT CHARACTER SELECTOR 

		# Get input without spamming
		events = pygame.event.get()
		for event in events:
		    if event.type == pygame.KEYDOWN:
		        if event.key == pygame.K_LEFT:
		            ruleSelected -=1
		            valueSelected = 0
		        if event.key == pygame.K_RIGHT:
		            ruleSelected +=1
		            valueSelected = 0
		        if event.key == pygame.K_UP:
		            valueSelected +=1
		        if event.key == pygame.K_DOWN:
		            valueSelected -=1
		        if event.key == pygame.K_b:
		            rulesOptions = False
		        if event.key == pygame.K_c:
		            ruleConfirmed = True



		if(ruleSelected > len(rulesArray) - 1): ruleSelected=0
		if(ruleSelected < 0): ruleSelected = len(rulesArray) - 1

		if(chosenRule == 'gossipStimulation'):
			ruleValue = str(int(ruleValue) + (valueSelected * 5))
			if(int(ruleValue) <0): ruleValue=abs(int(ruleValue))
		if(chosenRule == 'talkingDistance'):
			ruleValue = str(int(ruleValue) + (valueSelected * 5))
			if(int(ruleValue) <0): ruleValue=abs(int(ruleValue))
		if(chosenRule == 'luckyChance'):
			ruleValue = str(int(ruleValue) + (valueSelected * 100))
			if(int(ruleValue) <0): ruleValue=abs(int(ruleValue))
		if(chosenRule == 'citizenWalkSpeed'):
			ruleValue = str(int(ruleValue) + (valueSelected * 1))
			if(int(ruleValue) <0): ruleValue=abs(int(ruleValue))

		# Update chosen value
		if(ruleConfirmed):
			updateRule(rulesFile,chosenRule,ruleValue)
			ruleConfirmed = False
			valueSelected = 0

		# ------------TICK FRAMES

		if (gameClock > nextFrame):
			backgroundFrame = (backgroundFrame+1)%11
			nextFrame += 60



		# -------------DRAW

		# BACKGROUND
		draw_back(SCREEN,backgroundArray[backgroundFrame],x=0,y=0)
		
		# ARROW 
		draw_back(SCREEN,imageDict['arrowLeft'],x=80,y=HEIGHT/2)
		draw_back(SCREEN,imageDict['arrowRight'],x=WIDTH - 80,y=HEIGHT/2)



		drawText(SCREEN,bigMenuFont,'Rules', 0.38*WIDTH,100)

		# PRINT RULE AND IT'S VALUE 
		drawText(SCREEN,bigMenuFont,chosenRule , 0.16*WIDTH,200)
		drawText(SCREEN,bigMenuFont,'Value: ', 0.16*WIDTH,240)
		drawText(SCREEN,bigMenuFont,'             ' + str(ruleValue) , 0.16*WIDTH,240,color=(218,165,32))


		# PRINT DESCRIPTION
		# ruleSelected is still used as an index
		chosenDesc = str(rulesDesc[ruleSelected].split(':')[1])

		rowLen,maxRL,words,i = 0,45,"",0
		if(len(chosenDesc) <= maxRL):
			drawText(SCREEN,bigMenuFont,str(chosenDesc),0.16*WIDTH,300)
		else:
			for word in chosenDesc.split():
				words+= word + ' '
				if(len(words) >= maxRL):
					drawText(SCREEN,bigMenuFont,str(words),0.16*WIDTH, (300 + (i * 40) ))
					words = ""
					i+=1
			if(words!=""): drawText(SCREEN,bigMenuFont,str(words),0.16*WIDTH,(300 + (i * 40) ) )

		





		drawText(SCREEN,menuFont,'[C] Confirm', 0.6*WIDTH,0.9*HEIGHT)
		drawText(SCREEN,menuFont,'[B] Back', 0.8*WIDTH,0.9*HEIGHT)


		update()
		clock.tick(FPS)
		# 

