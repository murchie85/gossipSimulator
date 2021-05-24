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



from .processGossip import *
import random
from .rules import *
from ._DOS_citizen_functions import *





def processMovement(citizen,position):

	stepValue = random.randint(-10,10)

	# occasionally stop
	chance = random.randint(0,4)
	if(chance == 2): stepValue = 0

	newPosition = position + stepValue

	if newPosition > 1000: 
		newPosition = newPosition - 1000
		
	if newPosition < 0: newPosition = 1000 - newPosition


	return(newPosition)



def gossipDecision(citizen,citizen_list,key,gossip_database,gossip_file,gossipObject,position,LOG_DICT):
	# ACTION    ------CREATE GOSSIP & UPDATE KNOWN RUMOURS------

	# TODO: Ensure action is checked to be empty when spreading/gossiping
	## CHECK IF POSTION IS NEAR THEN SHARE GOSSIP
	thisCitizen = citizen
	myPosition = position

	# don't go thru list in same order every time
	keys = list(citizen_list.keys())
	random.shuffle(keys)
	# loop other citizen
	for key in keys:
		other_citizen                  = citizen_list[key]
		if(other_citizen == thisCitizen): continue



		# THIS WILL BE DIFFERENT IN GAME VERSION 
		other_citizen_position    = other_citizen['location']
		distanceApart = getDistanceApart(myPosition,other_citizen_position,thisCitizen,other_citizen)




		# GET RULES
		gossipStimulation = int(getRules("rules/RULES.txt",'gossipStimulation'))
		talkingDistance   = int(getRules("rules/RULES.txt",'talkingDistance'))
		luckyChance       = int(getRules("rules/RULES.txt",'luckyChance'))

		# PARAMETERS 
		chance       = random.randint(0,int(gossipStimulation))
		
		# Create Chance 
		createGossipProbability = thisCitizen['CGP']
		createChance = createGossipProbability + chance

		# Spread Chance 
		spreadGossipProbability = thisCitizen['SGP']
		spreadChance = spreadGossipProbability + chance


		# Luck in general
		luckyChance  = random.randint(0,luckyChance)

		# RULE 
		# prevent them from just gossiping to the same person every time 
		# This works for create/spread but not for new ones
		if(limitGossipWithSamePerson(thisCitizen,other_citizen) == 'False'): return(citizen,citizen_list,gossip_database,gossipObject)


		citizenChoice = random.choice(['createGos','spreadGos'])
		
		# CREATE GOSSIP 
		if(citizenChoice=='createGos'): citizen,gossip_database, gossipObject,citizen_list = createGossip(citizen,citizen_list,gossip_database,gossipObject,createChance,other_citizen,distanceApart,talkingDistance,luckyChance,gossip_file,LOG_DICT)

		# SPREAD GOSSIP
		if(citizenChoice=='spreadGos'): citizen,gossip_database, gossipObject,citizen_list = spreadGossip(citizen,citizen_list,gossip_database,gossipObject,spreadChance,other_citizen,distanceApart,talkingDistance,luckyChance,gossip_file,LOG_DICT)





	return(citizen,citizen_list,gossip_database,gossipObject)



def createGossip(citizen,citizen_list,gossip_database,gossipObject,createChance,other_citizen,distanceApart,talkingDistance,luckyChance,gossip_file,LOG_DICT):
	
	# WONT GOSSIP AGAIN UNTIL COUNTER IS RESET
	citizenAction = citizen['action']
	if(('gossiping' in str(citizen['action'])) or ('receiving' in str(citizen['action'])) or ('spreading' in str(citizen['action'])) ):
			return(citizen,gossip_database, gossipObject,citizen_list)
	
	# CREATE RUMOUR 
	if((createChance > 80) and (distanceApart < talkingDistance) or (distanceApart < talkingDistance and luckyChance == 10)):
		
		# Creates a gossip object
		gossip_database, gossipObject = createRumour(gossip_database, citizen_list, creator=citizen['name'], gossip_file=gossip_file)  
		
		# updates SELF: the fishwifes internal reference
		citizen_list,gossip_database = updateKnownRumours(citizen_list,citizen, other_citizen ,gossipObject,gossip_database, 'create',LOG_DICT)

		# Reciever accepts rumour (at a given trust value)
		citizen_list,gossip_database = updateKnownRumours(citizen_list,citizen, other_citizen ,gossipObject,gossip_database, 'acceptRumour',LOG_DICT)

		# put action = ['gossiping',5]
		# TODO manage the clash for recieving and gossiping at same time.
		# this is different from citizen['known_rumours']['action'] 
		citizen['action']        = ['gossiping',20]
		other_citizen['action']  = ['receiving',15]

	return(citizen,gossip_database, gossipObject,citizen_list)


def spreadGossip(citizen,citizen_list,gossip_database,gossipObject,spreadChance,other_citizen,distanceApart,talkingDistance,luckyChance,gossip_file,LOG_DICT):

	# WONT GOSSIP AGAIN UNTIL COUNTER IS RESET
	citizenAction = citizen['action']
	if(('gossiping' in str(citizen['action'])) or ('receiving' in str(citizen['action'])) or ('spreading' in str(citizen['action'])) ):
			return(citizen,gossip_database, gossipObject,citizen_list)

	if(len(citizen['knownRumours']) <1): return(citizen,gossip_database, gossipObject,citizen_list)

	
	# SPREAD RUMOUR 
	# if spread high trigger
	# check if existing gossip exists 
	# select a rumour to spread
	# update internal reference using 'spread'
	# ONLY SPREAD ACTIVE RUMOURS
	if((spreadChance > 100) and (distanceApart < talkingDistance) or (distanceApart < talkingDistance and luckyChance == 10)):


		# CONDITION TO DOCUMENT
		# FILTER ACTIVE ONLY
		tempArray = [x for x in citizen['knownRumours'] if citizen['knownRumours'][x]['status'] == 'active']
		tempDict = {}
		for key in tempArray: tempDict[key] = citizen['knownRumours'][key]
		
		# Want to spread but no rumours to spread 
		if(len(tempDict) <1): return(citizen,gossip_database, gossipObject,citizen_list)
		
		# Get highest sensationalism index
		chosenIndex  = max(tempDict, key=lambda x: tempDict[x]['sensationalism'])
		chosenGossip = citizen['knownRumours'][chosenIndex]


		gossipObject = gossip_database[str(chosenIndex)]

		# updates SELF: the fishwifes internal reference
		citizen_list,gossip_database = updateKnownRumours(citizen_list,citizen, other_citizen ,gossipObject,gossip_database, 'spread',LOG_DICT)

	return(citizen,gossip_database, gossipObject,citizen_list)


	