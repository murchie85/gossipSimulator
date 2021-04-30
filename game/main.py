import pygame
import os
import time
import math
import random
 
## Internal game libraries
from functions._game_config import *
from functions._game_functions import *
from functions._game_options import *
from functions._game_start_game import *

## Internal libraries
from functions.utils import *
from functions.printer import *
from functions.processGossip import *  
from functions.create_citizen import *
from functions.botDecisionTree import *
from functions.logging import *


if os.path.exists("logs/gossip.txt"):os.remove("logs/gossip.txt")
if os.path.exists("recieve-gossip.csv"):os.remove("recieve-gossip.csv")


#-----------------GAME VARIABLES-------------------
#pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Celestus")


# Level: OpenFoyer
obj1          = pygame.Rect(347,412,110,96)
wallone  = pygame.Rect( 289, 599, (153),(60) )
walltwo  = pygame.Rect( 290, 410, 20, 244)
wallthree  = pygame.Rect(495 , 408,79 , 245)
wallfour  = pygame.Rect( 291, 223, 112, 125)
wallfive  = pygame.Rect( 456, 222,115 ,120 )
wallsix  = pygame.Rect( 197, 301,113, 58)
wallseven  = pygame.Rect( 198, 411,113 ,55 )
walleight     = pygame.Rect(141 ,411 ,71 ,136 )
wallnine      = pygame.Rect( 197, 167, 23, 191)
wallten       = pygame.Rect( 159, 170, 42,108 )
walleleven    = pygame.Rect( 159, 0,22 ,180 )
walltwelth    = pygame.Rect( 84, 0,22 , 172)
wallthirteen  = pygame.Rect( 29, 168, 76, 50)
wallfourteen  = pygame.Rect( 66, 173, 39, 105)
wone  = pygame.Rect( 29, 167,22 , 380)
wtwo  = pygame.Rect( 43, 436, 43,112 )
wthree = pygame.Rect( 84,491 ,22 ,57 )
wfour  = pygame.Rect( 364, 145,22 ,86 )
wfive  = pygame.Rect( 364, 0,22 ,84 )
wsix    = pygame.Rect( 475,148 , 21,80)
wseven  = pygame.Rect( 476, 0,22 , 84)
weight  = pygame.Rect( 552,408 ,207 , 59)
wnine  = pygame.Rect( 551, 302, 115, 55)
wten  = pygame.Rect( 643,222 ,25 ,130 )
weleven  = pygame.Rect( 643, 221, 133,80 )
wtwelve  = pygame.Rect( 756, 86, 23,205 )
wthirteen  = pygame.Rect( 643,85 ,134 ,60 )
wfourteen  = pygame.Rect(830 , 87, 132,58 )
aone  = pygame.Rect(831 , 843,22 ,141 )
atwo  = pygame.Rect( 830, 221, 76, 83)
athree  = pygame.Rect( 887, 222, 22,350 )
afour  = pygame.Rect(793 , 356,111 ,110 )
afive  = pygame.Rect(644 ,516, 263, 58)
asix = pygame.Rect( 643,410 ,22 ,160 )
aseven = pygame.Rect( 700, 450,22 , 76)
aeight = pygame.Rect(  831,  85,22  , 211 )




backgroundObjectMasks    = [obj1,wallone,walltwo,wallthree,wallfour,wallfive,wallsix,wallseven,walleight,
							wallnine,wallten,walleleven,walltwelth,wallthirteen,wallfourteen,wone,wtwo,wthree,
							wfour,wfive,wsix,wseven,weight,wnine,wten,weleven,wtwelve,wthirteen,wfourteen,
							aone,atwo,athree,afour,afive,asix,aseven,aeight]



#**************************************  
#    ---------SIM VARIABLES  -----  
#*************************************** 

# Set up Time
game_time      = 0
day_len        = 60
month_len      = 28 * day_len
time_increment = 1





# Citizens
numberOfCitizens = 15
# Files
gossip_file = "gossip/mvpGossip.txt"
#spritePath  = '/Users/adammcmurchie/2021/fishwives/sprites/characters/'
#spriteNames = ['claude.gif']

#--------------------
## DATABASE CREATION 
#--------------------
#citizen_list = generateCitizens(15)
citizen_list = {}
gossip_database = {}





def main(citizen_list,numberOfCitizens,sprite_frame=0):
	#************************************************************************************
	#
	#              ---------------INITIALISATION--------------                          *
	#
	#************************************************************************************

	# -----DOS FIELDS
	gossip_database = {}
	message           = ""
	messageTime       = 5
	# gossip
	gossipObject      = ""
	gossipUpdates     = []
	displayGossipTime = 5
	collidingObjects  = []
	chosenGossip      = ""

	# ------PYGAME FIELDS
	moving = 0
	SCREEN.fill((0,0,0))
	ark_pos     = pygame.Rect(WIDTH/2,HEIGHT/2,tileSize/2,tileSize/2)
	
	clock       = pygame.time.Clock()
	run         = True                 # When False game exits
	gameCounter = 0                    # loop count 
	frameSwitch = 0                    # var to let us know the frame has been switched and to wait
	FPS         = 15                   # PS
	facing      = 'down'
	nextFrame   = pygame.time.get_ticks()
	citizen_list = startGame(FPS,SCREEN,menuFont,citizen_list,numberOfCitizens, WIDTH,HEIGHT)
	noticationStatus = ""
	# initialise bot characteristics
	for key in citizen_list:
		citizen  = citizen_list[key]
		citizen = initializeMovement(citizen,botSprites)





	#************************************************************************************
	#
	#              ---------------IN GAME---------------                          *
	#
	#************************************************************************************



	while run: 
		gameCounter      += 1
		timeCounter      = round(pygame.time.get_ticks()/1200)
		gameClock        = pygame.time.get_ticks()


		#************************************************************************************
		#
		#              ---------------BOT ACTIONS---------------                          *
		#
		#************************************************************************************
		citizenArray = []
		for key in citizen_list: citizenArray.append(citizen_list[key])
		# Loop Citizens 
		for key in citizen_list:
			citizen                        = citizen_list[key]
			position                       = citizen['movement']['pos']
			gossipObject                   = {} # flush every time 

			#  ------WALK------
			citizen = processMovement(citizen,citizen_list,position,BOTVEL,WIDTH,HEIGHT,backgroundObjectMasks)
			# ------CREATE GOSSIP & UPDATE KNOWN RUMOURS------
			citizen,citizen_list,gossip_database,gossipObject = gossipDecision(citizen,citizen_list,key,gossip_database,gossip_file,gossipObject,citizen['movement']['pos'])
			# UPATES
			if (len(gossipObject) > 0): gossipUpdates.append(gossipObject)

















		#************************************************************************************
		#
		#              ---------------USER ACTIONS----------------                          *
		#
		#************************************************************************************

		#-- GET KEYPRESS
		keys_pressed = pygame.key.get_pressed()
		ark_pos, facing, moving = moveSprite(keys_pressed,ark_pos,VEL,facing,moving,WIDTH,HEIGHT,citizen_list,backgroundObjectMasks)

		#---MENU
		if keys_pressed[pygame.K_o]: options(FPS,SCREEN,myfont,menuFont,citizen_list,gossip_database,WIDTH,HEIGHT)
		if keys_pressed[pygame.K_c]: run = False     # QUIT GAME

		# SPRITE 
		# This was hard to do, you have to put next frame forward a certain amount
		if (gameClock > nextFrame):
			sprite_frame = (sprite_frame+1)%3
			nextFrame += 120


		#************************************************************************************
		#
		#              ---------------DRAW SECTION----------------                          *
		#
		#************************************************************************************

		drawWindow(SCREEN)
		draw_back(SCREEN,mainBack,x=0,y=0)
		"""
		for item in backgroundObjectMasks:
			pygame.draw.rect(SCREEN, (255,255,255), item)
		
		"""
		#-----DRAW SPRITES

		draw_sprite(SCREEN, Ark,ark_pos,moving,facing,sprite_frame)
		for key in citizen_list:
			citizen  = citizen_list[key]
			draw_sprite(SCREEN, citizen['sprite'],citizen['movement']['pos'],citizen['movement']['moving'],citizen['movement']['facing'],sprite_frame)
			
			# Print Gossip bubble
			citizenAction = citizen['action']
			if(len(citizenAction) > 0):
				if(citizenAction[0] == 'gossiping'):
					citizenAction[1] = (citizenAction[1] -1)
					draw_speechBubble(SCREEN,myfont,citizen['movement']['pos'].x , citizen['movement']['pos'].y  -32, 'Rumour!')
					# reset once it hits 0
					if(citizenAction[1] <1):
						citizen['action'] = []

			# Print Gossip bubble
			citizenAction = citizen['action']
			if(len(citizenAction) > 0):
				if(citizenAction[0] == 'receiving'):
					citizenAction[1] = (citizenAction[1] -1)
					draw_speechBubble(SCREEN,myfont,citizen['movement']['pos'].x , citizen['movement']['pos'].y  -32, 'Really?')
					# reset once it hits 0
					if(citizenAction[1] <1):
						citizen['action'] = []



		#************************************************************************************
		#
		#              ---------------DEBUG PRINT----------------                          *
		#
		#************************************************************************************

		draw_backScaled(SCREEN,Dialoguebox,0.028*WIDTH, 0.085*HEIGHT ,170,60)
		drawText(SCREEN,myfont,str("TIME: " + str(timeCounter)),0.05*WIDTH, 0.1*HEIGHT)
		for key in citizen_list:
			kt = sum(len(x['knownRumours']) for x in citizen_list.values() if x)
			out = 'Known Rumours: ' + str(kt)
			#out = "known Rumours are: " + str(len(citizen_list[key]['knownRumours']))	
		drawText(SCREEN,myfont,str(out),0.05*WIDTH, 0.14*HEIGHT)

		# Choses a random gossip string to write, skips if no new updates
		chosenGossip = logRandomUpdate(gossipUpdates,chosenGossip,'logs/gossip.txt')
		#************************************************************************************
		#
		#              ---------------NOTIFICATIONS----------------                          *
		#
		#************************************************************************************


		# ------UPDATE NOTIFICATION TIMER 
		noticationStatus,messageTime = printNotification(message, messageTime,SCREEN,WIDTH,HEIGHT,Dialoguebox)

		# PRINT A NOTIFICATION
		if((len(gossipUpdates) > 0)):
			if(noticationStatus == "free"):
				with open('logs/gossip.txt', 'r') as f:
					lines = f.read().splitlines()
					last_line = lines[-1]
					message = str(last_line)
					messageTime = 40
					gossipUpdates = []
					f.close()












		update()
		run = events(run)
		clock.tick(FPS)

	pygame.quit()
	print('Exiting...')
























if __name__ == '__main__':
	main(citizen_list,numberOfCitizens)