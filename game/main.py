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
if os.path.exists("recieve-gossip.csv"):os.remove("logs/recieve-gossip.csv")
if os.path.exists("recieve-gossip.csv"):os.remove("logs/gossipAction.txt")


#-----------------GAME VARIABLES-------------------
pygame.display.set_caption("Celestus")
#pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Level: OpenFoyer
from functions._game_level_one import *

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


#--------------------
## DATABASE CREATION 
#--------------------
#citizen_list = generateCitizens(15)
citizen_list = {}
gossip_database = {}





def main(citizen_list,numberOfCitizens,sprite_frame,vec, offset, offset_float,CONST, snap, keydown,moving, ark_pos, clock,run,gameCounter,frameSwitch,FPS,facing,nextFrame,noticationStatus):
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


	#pygame
	citizen_list = startGame(FPS,SCREEN,menuFont,citizen_list,numberOfCitizens, WIDTH,HEIGHT)
	spriteCounter = 0
	SCREEN.fill((0,0,0))

	# initialise bot characteristics
	for key in citizen_list:
		citizen  = citizen_list[key]
		citizen,spriteCounter = initializeMovement(citizen,botSprites,backgroundObjectMasks,spriteCounter)
		spriteCounter+=1





	#************************************************************************************
	#
	#              ---------------IN GAME---------------                          *
	#
	#************************************************************************************



	while run: 
		gameCounter      += 1
		timeCounter      = round(pygame.time.get_ticks()/1200)
		gameClock        = pygame.time.get_ticks()
		keys_pressed = pygame.key.get_pressed()
		snap,keydown = snapView(snap,keydown)

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
		# Update Camera
		offset,offset_float = scroll(ark_pos,offset,offset_float,CONST)
		# background
		draw_back(SCREEN,mainBack,0,0,snap,offset,2)
		#draw_back(SCREEN,mainBack,0,0,offset)
		"""
		for item in backgroundObjectMasks:
			pygame.draw.rect(SCREEN, (255,255,255), item)
		
		"""
		#-----DRAW SPRITES
		# Ark
		draw_sprite(SCREEN, Ark,ark_pos,moving,facing,sprite_frame,snap,offset,2)
		#draw_sprite(SCREEN, Ark,ark_pos,moving,facing,sprite_frame,offset)
		# Sprites
		for key in citizen_list:
			citizen  = citizen_list[key]
			draw_sprite(SCREEN, citizen['sprite'],citizen['movement']['pos'],citizen['movement']['moving'],citizen['movement']['facing'],sprite_frame,snap,offset,2)
			#draw_sprite(SCREEN, citizen['sprite'],citizen['movement']['pos'],citizen['movement']['moving'],citizen['movement']['facing'],sprite_frame,offset)
			
			# Print Gossip bubble
			citizenAction = citizen['action']
			if(len(citizenAction) > 0):
				if(citizenAction[0] == 'gossiping'):
					citizenAction[1] = (citizenAction[1] -1)
					draw_speechBubble(SCREEN,fonts,citizen['movement']['pos'].x , citizen['movement']['pos'].y  -32, 'Rumour!',sprite_frame,snap,offset)
					# reset once it hits 0
					if(citizenAction[1] <1):
						citizen['action'] = []

			# Print Gossip bubble
			citizenAction = citizen['action']
			if(len(citizenAction) > 0):
				if(citizenAction[0] == 'receiving'):
					citizenAction[1] = (citizenAction[1] -1)
					draw_speechBubble(SCREEN,fonts,citizen['movement']['pos'].x , citizen['movement']['pos'].y  -32, 'Really?',sprite_frame,snap,offset)
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

		# PULL A NOTIFICATION
		if((len(gossipUpdates) > 0)):
			if(noticationStatus == "free"):
				randomLogfile = random.choice(['logs/gossip.txt','logs/gossipAction.txt'])
				with open(randomLogfile, 'r') as f:
					lines = f.read().splitlines()
					last_line = lines[-1]
					message = str(last_line)
					messageTime = 40
					gossipUpdates = []
					f.close()












		update()
		run,keydown = events(run,keydown)
		clock.tick(FPS)

	pygame.quit()
	print('Exiting...')
























if __name__ == '__main__':
	main(citizen_list,numberOfCitizens,sprite_frame,vec, offset, offset_float,CONST, snap, keydown,moving, ark_pos, clock,run,gameCounter,frameSwitch,FPS,facing,nextFrame,noticationStatus)