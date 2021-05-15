import random
import pygame
from ._game_config import * 

def initializeMovement(citizen,botSprites,backgroundObjectMasks,spriteCounter):



		# If position collides, try another random pos

		noCol = False
		while(noCol==False):

			# Initialise a position on the map
			xpos = random.randint(int(0.1*WIDTH),int(0.9*WIDTH))
			ypos = random.randint(int(0.1*HEIGHT),int(0.9*HEIGHT))
			charRect = pygame.Rect(xpos,ypos,tileSize,tileSize)
			noCol = True
			# if everything is fine this will pass through
			for background in backgroundObjectMasks:
				if(charRect.colliderect(background)):
					noCol = False




		citizen['movement'] =  {"pos": charRect,
								"direction": 'none',
								"walkDuration": 0,
								"facing": 'down',
								"moving": 0}



		"""
		spritecounter is two counters in an array
		firstindex= male, secondindex=female
		the increment for the respective botsprite array
		which also has two nested arrays, one for male sprites
		the other for female
		by ticking through, we don't have too many of the same sprites
		if we overshoot, it goes back to zero
		"""
		gender = citizen['gender']
		if(gender=='male'):    
			citizen['sprite'] = botSprites[0][spriteCounter[0]]
			spriteCounter[0] +=1
			if(spriteCounter[0]>=len(botSprites[0])): spriteCounter[0]=0
		if(gender=='female'): 
			citizen['sprite'] = botSprites[1][spriteCounter[1]]
			spriteCounter[1] +=1
			if(spriteCounter[1]>=len(botSprites[1])): spriteCounter[1]=0

		
		return(citizen,spriteCounter)


def processMovement(citizen,citizen_list,position,BOTVEL,WIDTH,HEIGHT,backgroundObjectMasks):
	# Updating top level location value (not rect vals)
	citizen['location']             = [position.x,position.y]

	# ---------WALK THE BOTS
	citizen['movement']['direction'] ,citizen['movement']['walkDuration'] = botWalkBehaviour(citizen['movement']['direction'] ,citizen['movement']['walkDuration'])
	citizen['movement']['pos'], citizen['movement']['direction'], citizen['movement']['facing'] = moveBotSprite(citizen['movement']['pos'],citizen['movement']['direction'],BOTVEL,citizen['movement']['facing'],citizen,citizen_list,WIDTH,HEIGHT,backgroundObjectMasks)
	

	if(citizen['movement']['direction']!= 'none'):
		citizen['movement']['moving'] = 1
	else:
		citizen['movement']['moving'] = 0

	return(citizen)


def getDistanceApart(myPosition,other_citizen_position,thisCitizen,other_citizen):
	#distanceApart             = abs(myPosition - other_citizen_position)
	xdistance = abs(myPosition.x - other_citizen_position.x)
	ydistance = abs(myPosition.y - other_citizen_position.y)

	distanceApart = (xdistance + ydistance)/2

	return(distanceApart)
