import pygame
import os
import time
import math
import random
import pprint



## Internal game libraries
from functions._game_config import *
from functions._game_functions import *
from functions._game_options import *
from functions._game_start_game import *
from functions._game_sprite_functions import *
from functions._game_draw import *

## Internal libraries
from functions.utils import *
from functions.processGossip import *  
from functions.processCitizen import *
from functions.botDecisionTree import *
from functions.logging import *
from functions.rules import *



GOSSIP_LOGFILE        = "logs/LOGS_gossip.txt"
RECEIVE_LOGFILE       = "logs/LOGS_recieved-gossip.csv"
GOSSIP_ACTIONS        = "logs/LOGS_gossip_actions.txt"

DATABASE_CITIZENLIST  = "logs/DATABASE_CitizensList.txt"
DATABASE_GOSSIP       = "logs/DATABASE_Gossip.txt"

LOG_DICT ={"GOSSIP_LOGFILE":GOSSIP_LOGFILE,"RECEIVE_LOGFILE": RECEIVE_LOGFILE, "DATABASE_CITIZENLIST": DATABASE_CITIZENLIST,"DATABASE_GOSSIP":DATABASE_GOSSIP,"GOSSIP_ACTIONS":GOSSIP_ACTIONS}



if os.path.exists(GOSSIP_LOGFILE):os.remove(GOSSIP_LOGFILE)
if os.path.exists(RECEIVE_LOGFILE):os.remove(RECEIVE_LOGFILE)
if os.path.exists(GOSSIP_ACTIONS):os.remove(GOSSIP_ACTIONS)
if os.path.exists(DATABASE_CITIZENLIST):os.remove(DATABASE_CITIZENLIST)
if os.path.exists(DATABASE_GOSSIP):os.remove(DATABASE_GOSSIP)


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
gossip_file = "gossip/gossipDict.txt"
rulesFile   = 'rules/RULES.txt'

#--------------------
## DATABASE CREATION 
#--------------------
#citizen_list = generateCitizens(15)
citizen_list = {}
gossip_database = {}





def main(citizen_list,numberOfCitizens,sprite_frame,vec, offset, offset_float,CONST, snap, keydown,moving, ark_pos, clock,run,gameCounter,frameSwitch,FPS,facing,nextFrame,noticationStatus,LOG_DICT,imageDict,rulesFile):
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


	# Generates citizens once start selected
	citizen_list = startGame(FPS,SCREEN,menuFont,citizen_list,numberOfCitizens, WIDTH,HEIGHT,LOG_DICT['RECEIVE_LOGFILE'])
	spriteCounter = [0,0]
	SCREEN.fill((0,0,0))

	# initialise bot characteristics
	for key in citizen_list:
		citizen  = citizen_list[key]
		citizen,spriteCounter = initializeMovement(citizen,botSprites,backgroundObjectMasks,spriteCounter)




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
		BOTVEL       = int(getRules(rulesFile,'citizenWalkSpeed'))

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
			citizen_list                   = processEmotion(citizen,citizen_list,numberOfCitizens)
			citizenAction 				   = citizen['action']

			#  ------WALK------
			citizen = processMovement(citizen,citizen_list,position,BOTVEL,WIDTH,HEIGHT,backgroundObjectMasks)
			# ------CREATE GOSSIP & UPDATE KNOWN RUMOURS------
			citizen,citizen_list,gossip_database,gossipObject = gossipDecision(citizen,citizen_list,key,gossip_database,gossip_file,gossipObject,citizen['movement']['pos'],LOG_DICT)
			# UPATES
			if (len(gossipObject) > 0): gossipUpdates.append(gossipObject)

			
			# Tick down action Counter
			if(len(citizenAction) > 0):
				citizenAction[1] = (citizenAction[1] -1)
				if(citizenAction[1] <1): citizen['action'] = []

		
		# END CITIZEN LOOP
		gossip_database,citizen_list = reducePersistence(gossip_database,citizen_list,LOG_DICT)

		#************************************************************************************
		#
		#              ---------------USER ACTIONS----------------                          *
		#
		#************************************************************************************

		#-- GET KEYPRESS
		keys_pressed = pygame.key.get_pressed()
		ark_pos, facing, moving = moveSprite(keys_pressed,ark_pos,VEL,facing,moving,WIDTH,HEIGHT,citizen_list,backgroundObjectMasks)

		#---MENU
		if keys_pressed[pygame.K_o]: menu(FPS,SCREEN,myfont,menuFont,citizen_list,gossip_database,WIDTH,HEIGHT,imageDict)
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

		#-----DRAW SPRITES
		# Ark
		draw_sprite(SCREEN, Ark,ark_pos,moving,facing,sprite_frame,snap,offset,2)
		
		# Sprites
		for key in citizen_list:
			citizen  = citizen_list[key]
			draw_sprite(SCREEN, citizen['sprite'],citizen['movement']['pos'],citizen['movement']['moving'],citizen['movement']['facing'],sprite_frame,snap,offset,2)
			


			citizen['notifyTimer'] = citizen['notifyTimer'] -1
			citizenAction = citizen['action']

			if(citizen['notifyTimer'] < 10):
				# draw emotoin
				emotion = int(citizen['emotion'].split(',')[0])
				#draw_back(SCREEN,imageDict['speechBubble'],citizen['movement']['pos'].x -15,citizen['movement']['pos'].y -40 ,snap,offset,fudge=2,zoomhScale=2,zoomvScale=3, nhScale=1,nvScale=2)
				draw_back(SCREEN,imageDict['emojis'][emotion-1],citizen['movement']['pos'].x ,citizen['movement']['pos'].y -40 ,snap,offset,fudge=2,zoomhScale=2,zoomvScale=2, nhScale=1,nvScale=1)
				if(citizen['notifyTimer'] <0): citizen['notifyTimer'] = random.randint(50,200)
			elif(len(citizenAction) > 0):
				# Print Gossip bubble
				comment = ""
				if(citizenAction[0] == 'gossiping'): comment = 'Rumour!'
				if(citizenAction[0] == 'receiving'): comment = 'Really?'
				draw_speechBubble(SCREEN,fonts,imageDict,citizen['movement']['pos'].x , citizen['movement']['pos'].y  -32, comment,snap,offset)




		#************************************************************************************
		#
		#              ---------------DEBUG PRINT----------------                          *
		#
		#************************************************************************************
		# top left box
		draw_backScaled(SCREEN,Dialoguebox,0.028*WIDTH, 0.085*HEIGHT ,170,60)
		drawText(SCREEN,myfont,str("TIME: " + str(timeCounter)),0.05*WIDTH, 0.1*HEIGHT)
		kt = sum(len(x['knownRumours']) for x in citizen_list.values() if x)
		out = 'Known Rumours: ' + str(kt)
		drawText(SCREEN,myfont,str(out),0.05*WIDTH, 0.14*HEIGHT)

		# Choses a random gossip string to write, skips if no new updates
		chosenGossip = logRandomUpdate(gossipUpdates,chosenGossip,LOG_DICT['GOSSIP_LOGFILE'])


		# Save latest data structure
		pout = pprint.pformat(citizen_list, indent=4)
		logUpdateMessage(pout,DATABASE_CITIZENLIST,'w')

		# Save latest Gossip data structure
		pout = pprint.pformat(gossip_database, indent=4)
		logUpdateMessage(pout,DATABASE_GOSSIP,'w')
		#************************************************************************************
		#
		#              ---------------NOTIFICATIONS----------------                          *
		#
		#************************************************************************************


		# PRINT DIALOGUE BLUE BOX
		# ------UPDATE NOTIFICATION TIMER 
		noticationStatus,messageTime = printNotification(message, messageTime,SCREEN,WIDTH,HEIGHT,Dialoguebox,imageDict)

		# PULL A NOTIFICATION
		if((len(gossipUpdates) > 0)):
			if(noticationStatus == "free"):
				randomLogfile = random.choice([LOG_DICT["GOSSIP_LOGFILE"],LOG_DICT["GOSSIP_ACTIONS"]])
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
	main(citizen_list,numberOfCitizens,sprite_frame,vec, offset, offset_float,CONST, snap, keydown,moving, ark_pos, clock,run,gameCounter,frameSwitch,FPS,facing,nextFrame,noticationStatus,LOG_DICT,imageDict,rulesFile)