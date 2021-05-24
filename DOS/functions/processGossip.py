"""
# Program Name: create_gossip
# Author: Adam McMurchie
# DOC: 24 April 2021
# Summary: This program populates the gossip dict
#          by appending a new dict
# ***********ALL STATE IS STORED HERE******************
#


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



LOCAL 

		gossipID      = gossipObject['gossipID']
		action        = 'created'
		associated    = citizen_list[key]['name']
		trust         = int(0,100)
"""


import random 
from .logging import *
from .rules import *



def createRumour(gossip_database, citizen_list, creator,gossip_file):

	# initialise db if empty
	if len(gossip_database) == 0:
		gossipID = str(1)
	else:
		# strip keys, convert to ints, find the highest, add another
		gossipID = max([int(i) for i in [*gossip_database]]) + 1

	creator  = creator
	target   = random.choice([*citizen_list])

	# prevent it from being about self initially 
	while target == creator:
		target   = random.choice([*citizen_list])

	maxSentiment = int(getRules('rules/RULES.txt','reputationImpact'))
	sentiment           = random.randint(-maxSentiment,maxSentiment)
	


	# pull in some random gossip, this checks the size ot make sure we don't get empty string
	f = open(gossip_file)
	gossip =""
	gossipArray = f.read().split(';')
	while len(gossip) < 1:
		gossip              = random.choice(gossipArray)

	rumour              = gossip.replace('NAME', str(target))
	risk                = random.randint(0,100)
	sensationalism      = random.randint(0,100)
	persistence         = random.randint(0,500)
	spread_count        = 0
	associated_citizens = {}
	status 				= 'active'

	gossipObject = {
	'gossipID': str(gossipID),
	'creator': creator,
	'target': target,
	'sentiment': sentiment,
	'rumour': rumour,
	'risk': risk,
	'persistence': persistence,
	'sensationalism': sensationalism,
	'spread_count': spread_count,
	'associated_citizens':  associated_citizens,
	'status':  status,
	}

	gossip_database.update({str(gossipID): gossipObject})

	return(gossip_database, gossipObject)




"""
NOTES

Gossip object is just a row from the gossip global database 


"""

def updateKnownRumours(citizen_list,spreader, other_citizen,gossipObject,gossip_database, type,LOG_DICT):

	## THIS UPDATES THE CHARACTERS REFERENCE ONLY
	## ITS SUBJECTIVE BASED UPON THE ACTION
	# THE CREATOR KNOWS HE/SHE CREATED IT
	if type=='create':
		gossipID       = gossipObject['gossipID']
		action         = 'created'
		confidant      = other_citizen['name']
		sensationalism = gossipObject['sensationalism']
		trust          = 100
		spread_count   = 1
		status         = 'active'

		subjectiveGossip = {str(gossipID): {'action': action, 'confidant': confidant,'sensationalism':sensationalism, 'trust': trust,'spread_count':spread_count,'status':status }}
		# use the source name as key update spreader
		citizen_list[spreader['name']]['knownRumours'].update(subjectiveGossip)



	# UPDATE SELF 
	"""
	This could be someone who created
	or someone who recieved.
	The need to update the spread count
	they need to update who they will spread it to
	They need to update the latest action 
	"""
	if type=='spread':
		gossipID       = gossipObject['gossipID']
		action         = str(spreader['knownRumours'][gossipID]['action'] + 'S ')
		confidant      = other_citizen['name']
		spread_count   = spreader['knownRumours'][str(gossipID)]['spread_count'] + 1


		# UPDATE SPREADER
		citizen_list[spreader['name']]['knownRumours'][str(gossipID)]['action']       = action
		citizen_list[spreader['name']]['knownRumours'][str(gossipID)]['spread_count'] = spread_count
		citizen_list[spreader['name']]['knownRumours'][str(gossipID)]['confidant']    = confidant

		# UPDATE DATABASE spread count
		gossip_database[gossipID]['spread_count'] = gossip_database[gossipID]['spread_count'] + 1

		logUpdateMessage(str(spreader['name'] + ' spreaded a rumour for the ' + str(spread_count) + ' time \n'),LOG_DICT["GOSSIP_ACTIONS"])




	# the reciever knows the source
	if type=='acceptRumour':
		# TODO 
		# If I know this rumour, reject it 

		gossipID         = gossipObject['gossipID']
		if(gossipID  in other_citizen['knownRumours']):
			print('I already know this')
			input()
		action           = "Received"
		source           = spreader['name']
		sensationalism   = gossipObject['sensationalism']
		trust            = random.randint(0,65)
		spread_count     = 0
		status           = gossipObject['status']
		
		subjectiveGossip = {str(gossipID): {'action': action, 'source': source,'sensationalism':sensationalism, 'trust': trust, 'spread_count':0, 'status':status}}
		
		# UPDATE RECEIVER
		citizen_list[other_citizen['name']]['knownRumours'].update(subjectiveGossip)

		# AWARD STATUS POINTS
		sourceCitizensSP = citizen_list[spreader['name']]['SP']
		awardedSP        = round((1/random.randint(1,9)) * trust) # a fraction of trust
		totalSP          = sourceCitizensSP + awardedSP 
		rumourTarget    = gossipObject['target']
		sentiment       = gossipObject['sentiment']
		citizen_list[spreader['name']]['SP'] = totalSP


		# REPUTATION DAMAGE TO TARGET
		# status points change as a fraction of their original SP
		# modified by the sentiment
		tSP = citizen_list[rumourTarget]['SP']
		if(sentiment!=0): citizen_list[rumourTarget]['SP'] = round(tSP + ((sentiment/100)*abs(tSP)))

		# UPDATE SPREAD PERSISTENCE
		spreadPersistenceBoost = int(getRules("rules/RULES.txt",'spreadPersistenceBoost'))
		gossip_database[gossipID]['persistence'] = gossip_database[gossipID]['persistence'] + spreadPersistenceBoost

		# LOGGING
		logReceivedGossip(LOG_DICT["RECEIVE_LOGFILE"],gossipID,spreader['name'],other_citizen['name'],awardedSP,sourceCitizensSP,other_citizen['knownRumours'],citizen_list,rumourTarget,sentiment)
		# Random updates to log
		logUpdateMessage(str(spreader['name'] + ' told ' + str(other_citizen['name']) + ' a rumour. They received ' + str(awardedSP) + ' status points. They had ' + str(sourceCitizensSP) + ' \n'),LOG_DICT["GOSSIP_ACTIONS"])
		logUpdateMessage(str(str(rumourTarget) + ' was gosssiped about, the sentiment was ' + str(sentiment) + ' they had ' + str(tSP) + ' status points. They now have ' + str(citizen_list[rumourTarget]['SP'])+ ' \n' ),LOG_DICT["GOSSIP_ACTIONS"])


	return(citizen_list,gossip_database)

def reducePersistence(gossip_database,citizen_list,LOG_DICT):

	for gossip in gossip_database:
		dropOffRate = int(getRules("rules/RULES.txt",'dropOffRate'))
		originalPersistence = gossip_database[gossip]['persistence']
		gossip_database[gossip]['persistence'] = gossip_database[gossip]['persistence'] - dropOffRate

		# IF PERSISTENCE < 1; SET STATUS TO ACTIVE
		if(gossip_database[gossip]['persistence'] < 1):
			gossip_database[gossip]['status'] = 'dead'
			gossip_database[gossip]['persistence'] = 0
			for key in citizen_list:
				citizen  = citizen_list[key]
				if(gossip in citizen_list[key]['knownRumours']): 
					citizen_list[key]['knownRumours'][gossip]['status'] = 'dead'

			# LOG DEATH
			if(originalPersistence>0): logUpdateMessage(str("**Rumour is dead**, the rumour was " + str(gossip_database[gossip]['rumour']) + ' \n'),LOG_DICT["GOSSIP_ACTIONS"])
	return(gossip_database,citizen_list)

