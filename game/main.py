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
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
#pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Celestus")
myfont = pygame.font.Font("resources/nokiafc.ttf", 8)




VEL   = 5
Ark   = initialiseSprites(tileSize)





#----------------------------------------------------





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

#--------------------
## DATABASE CREATION 
#--------------------
#citizen_list = generateCitizens(15)
citizen_list = {}
gossip_database = {}


#----------------------------------------------------


# Print start 
#startMesssage(citizen_count,citizen_list)








def main(citizen_list,numberOfCitizens):
	gossip_database = {}
	# Initialisation
	SCREEN.fill((0,0,0))
	ark_pos = pygame.Rect(0,300,tileSize/2,tileSize/2)
	clock = pygame.time.Clock()
	run = True
	gameCounter = 0
	FPS = 60 
	facing = 'down'

	citizen_list = startGame(FPS,SCREEN,myfont,citizen_list,numberOfCitizens)


	while run:
		gameCounter += 1

		#-- BOT ACTIONS
		citizenArray = []
		for key in citizen_list: citizenArray.append(citizen_list[key])
		# Loop Citizens 
		for key in citizen_list:
			citizen                        = citizen_list[key]
			position                       = citizen['location']
			gossipObject                   = {} # flush every time 

			# later can make actins all within personality functions  

			# ACTION:   ------WALK------
			citizen_list[key]['location']  = moveCitizen(citizen,position)

		# ACTION    ------CREATE GOSSIP & UPDATE KNOWN RUMOURS------
		myVar = random.randint(0,200)
		if(myVar == 8):
			gossip_database, gossipObject = createRumour(gossip_database, citizen_list, creator=citizen['name'], gossip_file=gossip_file)  
			citizen_list = updateKnownRumours(citizen_list,key, gossipObject, type='create')
		





		#-- USER ACTIONS
		keys_pressed = pygame.key.get_pressed()
		
		#---KEYS
		if keys_pressed[pygame.K_o]: options(FPS,SCREEN,myfont)
		if keys_pressed[pygame.K_q]: run = False


		pos, facing = moveSprite(keys_pressed,ark_pos,VEL,facing)


		#--DRAW

		drawWindow(SCREEN)
		draw_sprite(SCREEN, Ark[facing],ark_pos)
		current_time = str(math.floor(gameCounter/30))
		drawText(SCREEN,myfont,current_time,0.05*WIDTH, 0.1*HEIGHT)
		#print(citizen_list[[*citizen_list][0]]['knownRumours'])
		for key in citizen_list:
			out = citizen_list[key]['knownRumours']
			
		drawText(SCREEN,myfont,str(out),0.05*WIDTH, 0.2*HEIGHT)
		
		update()
		run = events(run)


		clock.tick(FPS)




	pygame.quit()
	print('Exiting...')











if __name__ == '__main__':
	main(citizen_list,numberOfCitizens)