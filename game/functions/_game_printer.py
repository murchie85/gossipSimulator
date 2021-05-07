"""

This function prints row of 3 boxed 


"""
import math
import time
from art import *
from .utils import med_print
import pygame
from ._game_functions import *
from .logging import *
import random

blockLen     = 50
blocksPerRow = 3
updateFont = pygame.font.Font("resources/nokiafc.ttf", 16)

def stringMod(string,blockLen=50):
	allowedLen = blockLen - 4 # allow for | 
	difference = allowedLen - len(string)
	# pad with spaces
	if difference > 0:
		for i in range(0, difference):
			string += " "

	if difference < 0:
		string = string[:allowedLen]

	printString = "| " + string + " |"
	return(printString)



#  this will print a messages for a given time.
#  it counts down a timer to keep printing message
def printNotification(message, messageTime,SCREEN,WIDTH,HEIGHT,dialogueBox):
	if message == "":
		return('free',messageTime)

	if messageTime >= 0:

		# THIS DRAWS THE BACKGROUND DIALOGUE BOX
		draw_backScaled(SCREEN,dialogueBox,0.2*WIDTH,0.7*HEIGHT,600,120)

		# THIS WRITES ROWS IN EQUAL LENGTH, PREVENTS LETTER CUTOFF
		rowLen,maxRL,words,i = 0,42,"",0
		if(len(message) <= maxRL):drawText(SCREEN,updateFont,str(message),0.026*WIDTH, 0.735*HEIGHT)
		for word in message.split():
			words+= word + ' '
			if(len(words) >= maxRL):
				drawText(SCREEN,updateFont,str(words),0.26*WIDTH, (0.735 + (i * 0.05) )*HEIGHT)
				words = ""
				i+=1
		if(words!=""): drawText(SCREEN,updateFont,str(words),0.26*WIDTH,(0.735 + (i * 0.05) )*HEIGHT)

		messageTime -=1
		return('running',messageTime)

	if messageTime < 0:
		return('free',messageTime)



def logRandomUpdate(gossipUpdates,chosenGossip,filePath):
	if((len(gossipUpdates) > 0 )):
		oldGossip    = chosenGossip	
		if(oldGossip in gossipUpdates):
			return(chosenGossip)
		else:
			chosenGossip = random.choice(gossipUpdates)
			um = str('New Gossip: ' + str(chosenGossip['creator']) + " : " + str(chosenGossip['rumour'] + '\n'))
			logUpdateMessage(um,filePath)

	return(chosenGossip)


