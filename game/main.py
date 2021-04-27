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



#-----------------GAME VARIABLES-------------------
#pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Celestus")





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

	# ------PYGAME FIELDS
	moving = 0
	SCREEN.fill((0,0,0))
	ark_pos     = pygame.Rect(WIDTH/2,HEIGHT/2,tileSize/2,tileSize/2)
	
	clock       = pygame.time.Clock()
	run         = True                 # When False game exits
	gameCounter = 0                    # loop count 
	frameSwitch = 0                    # var to let us know the frame has been switched and to wait
	FPS         = 60                   # PS
	facing      = 'down'
	nextFrame   = pygame.time.get_ticks()
	citizen_list = startGame(FPS,SCREEN,menuFont,citizen_list,numberOfCitizens, WIDTH,HEIGHT)
	
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
		gameCounter += 1
		timeCounter = round(pygame.time.get_ticks()/1200)
		gameClock   = pygame.time.get_ticks()


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
			citizen = processMovement(citizen,citizen_list,position,BOTVEL,WIDTH,HEIGHT)
			# ------CREATE GOSSIP & UPDATE KNOWN RUMOURS------
			citizen,citizen_list,gossip_database,gossipObject = gossipDecision(citizen,citizen_list,key,gossip_database,gossip_file,gossipObject,citizen['location'])





















		#************************************************************************************
		#
		#              ---------------USER ACTIONS----------------                          *
		#
		#************************************************************************************

		#-- GET KEYPRESS
		keys_pressed = pygame.key.get_pressed()
		ark_pos, facing, moving = moveSprite(keys_pressed,ark_pos,VEL,facing,moving,WIDTH,HEIGHT)

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

		#-----DRAW SPRITES

		draw_sprite(SCREEN, Ark,ark_pos,moving,facing,sprite_frame)
		for key in citizen_list:
			citizen  = citizen_list[key]
			draw_sprite(SCREEN, citizen['sprite'],citizen['movement']['pos'],citizen['movement']['moving'],citizen['movement']['facing'],sprite_frame)






		#************************************************************************************
		#
		#              ---------------DEBUG PRINT----------------                          *
		#
		#************************************************************************************

		drawText(SCREEN,myfont,str("TIME: " + str(timeCounter)),0.05*WIDTH, 0.1*HEIGHT)
		for key in citizen_list:
			kt = sum(len(x['knownRumours']) for x in citizen_list.values() if x)
			out = 'Known Rumours: ' + str(kt)
			#out = "known Rumours are: " + str(len(citizen_list[key]['knownRumours']))	
		drawText(SCREEN,myfont,str(out),0.05*WIDTH, 0.14*HEIGHT)
		

		#************************************************************************************
		#
		#              ---------------NOTIFICATIONS----------------                          *
		#
		#************************************************************************************


		# ------UPDATE NOTIFICATION TIMER 
		noticationStatus,messageTime = printNotification(message, messageTime)

		# PRINT A NOTIFICATION
		if((len(gossipUpdates) > 0)):
			if(noticationStatus == "free"):
				with open('logs/gossip.txt', 'r') as f:
					lines = f.read().splitlines()
					last_line = lines[-1]
					message = str('😲😲**new gossip**😲😲 \n') +  last_line
					messageTime = 5
					gossipUpdates = []
					f.close()












		update()
		run = events(run)
		clock.tick(FPS)

	pygame.quit()
	print('Exiting...')
























if __name__ == '__main__':
	main(citizen_list,numberOfCitizens)