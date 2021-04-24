import pygame
import os
import time

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
myfont = pygame.font.SysFont('Comic Sans MS', 30)
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Celestus")
font = pygame.font.Font(pygame.font.get_default_font(), 36)
tileSize = 32

VEL = 10
Ark = initialiseSprites(tileSize)





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
	ark_pos = pygame.Rect(100,300,tileSize,tileSize)
	clock = pygame.time.Clock()
	run = True
	gameCounter = 0
	FPS = 100 
	citizen_list = generateCitizens(15)

	while run:
		clock.tick(FPS)
		gameCounter += 1
		run = events(run)

		keys_pressed = pygame.key.get_pressed()
		moveSprite(keys_pressed,ark_pos,VEL)

		
		draw(WIN, Ark,ark_pos)
		update()





	pygame.quit()
	print('Exiting...')



if __name__ == '__main__':
	main()