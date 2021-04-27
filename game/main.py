import pygame
import os
import time
import math
import random

## Internal game libraries
from functions.gameFunctions.config import *
from functions.gameFunctions.game_functions import *
from functions.gameFunctions.options import *
from functions.gameFunctions.start_game import *
from functions.gameFunctions.create_citizen import *
## Internal libraries
from functions.update_citizen import *
from functions.utils import med_print
from functions.printer import *
from functions.walk import *
from functions.create_gossip import *  



#-----------------GAME VARIABLES-------------------
pygame.font.init()
SCREEN  = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Celestus")
myfont   = pygame.font.Font("resources/nokiafc.ttf", 8)
menuFont = pygame.font.Font("resources/nokiafc.ttf", 16)




VEL    = 3
BOTVEL = 0.2
#Ark    = initialiseSprites(tileSize,'/Users/adammcmurchie/2021/fishwives/sprites/characters/ArkJ.gif')
Ark    = initialiseImageSpriteGroups('/Users/adammcmurchie/2021/fishwives/sprites/characters/ark/ark',12,32,32)
mainBackPath = "/Users/adammcmurchie/2021/fishwives/sprites/backgrounds/grass.png"
mainBack     = pygame.image.load(mainBackPath).convert()
mainBack     = pygame.transform.scale(mainBack, (WIDTH, HEIGHT))





#----------------------------------------------------



#---------------CREATING BOT SPRITES------------------------

spritePath  = '/Users/adammcmurchie/2021/fishwives/sprites/characters/'
spriteNames = ['ark','claude','Diane','Doug','Eberle','Ileyda','Jean','Philis','rick','Telmia','Vanrose','Yurald']
botSprites = []
for i in range(len(spriteNames)):
	path = spritePath + spriteNames[i] +'/' + spriteNames[i] 
	botSprite = initialiseImageSpriteGroups(path,9,32,32)
	botSprites.append(botSprite)





#-----------------SIM VARIABLES-------------------
# Set up Time
game_time      = 0
day_len        = 60
month_len      = 28 * day_len
time_increment = 1

# gossip
gossipObject      = ""
gossipUpdates     = []
displayGossipTime = 5

# print vars 
message           = ""
messageTime       = 5

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

	# MVP FIELDS
	gossip_database = {}


	# PYGAME FIELDS
	moving = 0
	SCREEN.fill((0,0,0))
	ark_pos     = pygame.Rect(WIDTH/2,HEIGHT/2,tileSize/2,tileSize/2)
	
	clock       = pygame.time.Clock()
	run         = True                 # When False game exits
	gameCounter = 0                    # loop count 
	frameSwitch = 0                    # var to let us know the frame has been switched and to wait
	FPS         = 60                   # PS
	facing      = 'down'               # direction facing as a number
	nextFrame   = pygame.time.get_ticks()
	citizen_list = startGame(FPS,SCREEN,menuFont,citizen_list,numberOfCitizens)
	
	# initialise bot characteristics
	for key in citizen_list:
		citizen  = citizen_list[key]
		citizen['movement'] =  {"pos": pygame.Rect(random.randint(int(0.1*WIDTH),int(0.9*WIDTH)),random.randint(int(0.1*HEIGHT),int(0.9*HEIGHT)),tileSize/2,tileSize/2),
								"direction": 'none',
								"walkDuration": 0,
								"facing": 'down',
								"moving": 0}
		citizen['sprite'] = random.choice(botSprites)








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
		#              -------------PROCESS CITIZEN---------------                          *
		#************************************************************************************
		citizenArray = []
		for key in citizen_list: citizenArray.append(citizen_list[key])
		# Loop Citizens 
		for key in citizen_list:
			citizen                        = citizen_list[key]
			position                       = citizen['movement']['pos']
			gossipObject                   = {} # flush every time 


			# Updating top level location value (not rect vals)
			citizen['location']             = [position.x,position.y]

			# ---------WALK THE BOTS
			citizen['movement']['direction'] ,citizen['movement']['walkDuration'] = botWalkBehaviour(citizen['movement']['direction'] ,citizen['movement']['walkDuration'])
			citizen['movement']['pos'], citizen['movement']['direction'], citizen['movement']['facing'] = moveBotSprite(citizen['movement']['pos'],citizen['movement']['direction'],BOTVEL,citizen['movement']['facing'],citizen,citizen_list)
			if(citizen['movement']['direction']!= 'none'):
				citizen['movement']['moving'] =1
			else:
				citizen['movement']['moving']=0

			# ACTION    ------CREATE GOSSIP & UPDATE KNOWN RUMOURS------
			myVar = random.randint(0,200)
			if(myVar == 8):
				gossip_database, gossipObject = createRumour(gossip_database, citizen_list, creator=citizen['name'], gossip_file=gossip_file)  
				citizen_list = updateKnownRumours(citizen_list,key, gossipObject, type='create')
			






		#************************************************************************************
		#
		#              ---------------USER ACTIONS----------------                          *
		#
		#************************************************************************************



		#-- GET KEYPRESS
		keys_pressed = pygame.key.get_pressed()
		ark_pos, facing, moving = moveSprite(keys_pressed,ark_pos,VEL,facing,moving)

		#---MENU
		if keys_pressed[pygame.K_o]: options(FPS,SCREEN,myfont,menuFont,citizen_list,gossip_database)
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
		



		update()
		run = events(run)


		clock.tick(FPS)




	pygame.quit()
	print('Exiting...')











if __name__ == '__main__':
	main(citizen_list,numberOfCitizens)