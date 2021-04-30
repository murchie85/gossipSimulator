"""




GLOBAL TRACKER
| Object                      | Values |
| ----------- | ----------- |
| **gossipID (key)**              | `string( int(value) )` value increments |
| **creator**                     | [citizen_list]name (Pkey) |
| **target**                      | [citizen_list]name (Pkey) |
| **sentiment** | `random(0,100)` |
| **rumour**                      | `string` |
| **risk**                        | `random(0,100)`|
| **persistence**                 | `random(0,100)` |
| **spread_count**              | `int(value)`value increments |
| **associated_citizens**         | initialised as `random(0,1000)` |

LOCAL TRACKER 

		gossipID      = gossipObject['gossipID']
		action        = 'created,recieved'
		associated    = citizen_list[key]['name']

"""




import pygame 
from ._game_config import *
from ._game_functions import *
from .processGossip import *
import random


 
def initializeMovement(citizen,botSprites):
		citizen['movement'] =  {"pos": pygame.Rect(random.randint(int(0.1*WIDTH),int(0.9*WIDTH)),random.randint(int(0.1*HEIGHT),int(0.9*HEIGHT)),tileSize,tileSize),
								"direction": 'none',
								"walkDuration": 0,
								"facing": 'down',
								"moving": 0}
		citizen['sprite'] = random.choice(botSprites)
		return(citizen)


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




def gossipDecision(citizen,citizen_list,key,gossip_database,gossip_file,gossipObject,position):
	# ACTION    ------CREATE GOSSIP & UPDATE KNOWN RUMOURS------

	## CHECK IF POSTION IS NEAR THEN SHARE GOSSIP
	thisCitizen = citizen
	myPosition = position

	# don't go thru list in same order every time
	keys = list(citizen_list.keys())
	random.shuffle(keys)
	for key in keys:
		other_citizen                  = citizen_list[key]
		if(other_citizen == thisCitizen): continue



		# THIS WILL BE DIFFERENT IN GAME VERSION 
		other_citizen_position    = other_citizen['movement']['pos']
		#distanceApart = getDistanceApart(myPosition,other_citizen_position,thisCitizen,other_citizen)
		distanceApart = getDistanceApart(myPosition,other_citizen_position,thisCitizen,other_citizen)




		# RANDOM CHANCE
		createGossipProbability = thisCitizen['CGP']
		gossipStimulation = getRules("rules.txt",'gossipStimulation')
		chance = random.randint(1,int(gossipStimulation))
		myChance = createGossipProbability + chance

		luckyChance = random.randint(0,10000)



		# CREATE AND SPREAD GOSSIP - working probability as this loops a lot in a short time. 
		# WONT GOSSIP AGAIN UNTIL COUNTER IS RESET

		citizenAction = citizen['action']
		if(('gossiping' in str(citizen['action'])) or ('receiving' in str(citizen['action']))): 
			return(citizen,citizen_list,gossip_database,gossipObject)


		if((myChance > 80) and (distanceApart < 50) or (distanceApart < 50 and luckyChance == 10)):
			#print(str(thisCitizen['name']) + ' and ' + str(other_citizen['name']) + ' are within ' + str(distanceApart) + ' of each other and about to gossip.')
			#print(str(thisCitizen['name']) + ' cgp= ' + str(createGossipProbability) + ' chance= ' + str(chance) )
			#print('lucky chance = ' + str(luckyChance))

			# Creates a gossip object
			gossip_database, gossipObject = createRumour(gossip_database, citizen_list, creator=citizen['name'], gossip_file=gossip_file)  
			
			# updates the fishwifes internal reference
			citizen_list = updateKnownRumours(citizen_list,citizen, other_citizen ,gossipObject, 'create')

			# Reciever accepts rumour (at a given trust value)
			citizen_list = updateKnownRumours(citizen_list,citizen, other_citizen ,gossipObject, 'acceptRumour')

			# put action = ['gossiping',5]
			# TODO manage the clash for recieving and gossiping at same time. 
			citizen['action']        = ['gossiping',15]
			other_citizen['action']  = ['receiving',15]


	return(citizen,citizen_list,gossip_database,gossipObject)


def getDistanceApart(myPosition,other_citizen_position,thisCitizen,other_citizen):
	#distanceApart             = abs(myPosition - other_citizen_position)
	xdistance = abs(myPosition.x - other_citizen_position.x)
	ydistance = abs(myPosition.y - other_citizen_position.y)

	distanceApart = (xdistance + ydistance)/2

	return(distanceApart)


def spreadGossip(myPosition,other_citizen_position,thisCitizen,other_citizen):
	distanceApart             = abs(myPosition - other_citizen_position)

	return(distanceApart)


def getRules(rulesFile,targetVar):
	f = open(rulesFile, "r")
	rules = f.read()
	rules = rules.split(',')
	for r in rules: 
		if(r.split(':')[0] == str(targetVar)):
			return(r.split(':')[1])

	print('Target variable not found in rules file')
	print('variable is: ' + str(targetVar))
	exit()
	