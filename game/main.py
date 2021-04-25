import pygame
import os
import time
import math

## Internal game libraries
from functions.config import *
from functions.game_functions import *

## Internal libraries
from functions.create_citizen import *
from functions.update_citizen import *
from functions.utils import med_print
from functions.printer import *
from functions.walk import *
from functions.create_gossip import *  



#-----------------GAME VARIABLES-------------------
pygame.font.init()
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Celestus")
myfont = pygame.font.Font("resources/PAPYRUS.TTF", 16)




VEL   = 10
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
citizen_count = 15

# Files
gossip_file = "gossip/mvpGossip.txt"

#--------------------
## DATABASE CREATION 
#--------------------
#citizen_list = generateCitizens(15)
gossip_database = {}


#----------------------------------------------------


# Print start 
#startMesssage(citizen_count,citizen_list)








def main():
	# Initialisation
	SCREEN.fill((0,0,0))
	ark_pos = pygame.Rect(0,300,tileSize/2,tileSize/2)
	clock = pygame.time.Clock()
	run = True
	gameCounter = 0
	FPS = 60 
	facing = 'down'



	while run:
		gameCounter += 1

		#-- ACTIONS
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_o]:
			options(FPS)
		pos, facing = moveSprite(keys_pressed,ark_pos,VEL,facing)


		#--DRAW

		drawWindow(SCREEN)
		draw_sprite(SCREEN, Ark[facing],ark_pos)
		current_time = str(math.floor(gameCounter/30))
		drawText(SCREEN,myfont,current_time)
		
		update()
		run = events(run)


		clock.tick(FPS)




	pygame.quit()
	print('Exiting...')

def options(FPS):
	# Initialisation
	SCREEN.fill((0,0,0))
	clock = pygame.time.Clock()
	optionRun = True



	while optionRun:
		drawText(SCREEN,myfont,'menu')

		#-- ACTIONS
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_g]:
			optionRun = False


		for event in pygame.event.get():
			if event.type == pygame.QUIT:optionRun = False

		update()
		clock.tick(FPS)





if __name__ == '__main__':
	main()