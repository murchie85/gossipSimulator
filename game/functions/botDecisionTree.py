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
from ._game_sprite_functions import *
from .processGossip import *
import random
from .rules import *




def gossipDecision(citizen,citizen_list,key,gossip_database,gossip_file,gossipObject,position,LOG_DICT):
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
		distanceApart = getDistanceApart(myPosition,other_citizen_position,thisCitizen,other_citizen)




		# GET RULES
		gossipStimulation = int(getRules("rules/RULES.txt",'gossipStimulation'))
		talkingDistance   = int(getRules("rules/RULES.txt",'talkingDistance'))
		luckyChance       = int(getRules("rules/RULES.txt",'luckyChance'))



		# PARAMETERS 
		createGossipProbability = thisCitizen['CGP']
		chance = random.randint(0,int(gossipStimulation))
		myChance = createGossipProbability + chance
		luckyChance = random.randint(0,luckyChance)




		# CREATE AND SPREAD GOSSIP - working probability as this loops a lot in a short time. 
		
		# WONT GOSSIP AGAIN UNTIL COUNTER IS RESET
		citizenAction = citizen['action']
		if(('gossiping' in str(citizen['action'])) or ('receiving' in str(citizen['action']))): 
			return(citizen,citizen_list,gossip_database,gossipObject)


		# RULE 
		# prevent them from just gossiping to the same person every time 
		if(limitGossipWithSamePerson(thisCitizen,other_citizen) == 'False'): return(citizen,citizen_list,gossip_database,gossipObject)


		# RULE 
		if((myChance > 80) and (distanceApart < talkingDistance) or (distanceApart < talkingDistance and luckyChance == 10)):

			# Creates a gossip object
			gossip_database, gossipObject = createRumour(gossip_database, citizen_list, creator=citizen['name'], gossip_file=gossip_file)  
			
			# updates the fishwifes internal reference
			citizen_list,gossip_database = updateKnownRumours(citizen_list,citizen, other_citizen ,gossipObject,gossip_database, 'create',LOG_DICT)

			# Reciever accepts rumour (at a given trust value)
			citizen_list,gossip_database = updateKnownRumours(citizen_list,citizen, other_citizen ,gossipObject,gossip_database, 'acceptRumour',LOG_DICT)

			# put action = ['gossiping',5]
			# TODO manage the clash for recieving and gossiping at same time. 
			citizen['action']        = ['gossiping',20]
			other_citizen['action']  = ['receiving',15]


	return(citizen,citizen_list,gossip_database,gossipObject)



def spreadGossip(myPosition,other_citizen_position,thisCitizen,other_citizen):
	distanceApart             = abs(myPosition - other_citizen_position)

	return(distanceApart)



	