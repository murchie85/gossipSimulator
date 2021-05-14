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
	persistence         = random.randint(0,100)
	spread_count        = 0
	associated_citizens = {}

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
	}

	gossip_database.update({str(gossipID): gossipObject})

	return(gossip_database, gossipObject)



def updateKnownRumours(citizen_list,spreader, other_citizen,gossipObject,gossip_database, type,LOG_DICT):

	## THIS UPDATES THE CHARACTERS REFERENCE ONLY
	## ITS SUBJECTIVE BASED UPON THE ACTION

	# THE CREATOR KNOWS HE/SHE CREATED IT
	if type=='create':
		gossipID      = gossipObject['gossipID']
		action        = 'created'
		confidant     = other_citizen['name']
		sensationalism = gossipObject['sensationalism']
		trust         = 100

		subjectiveGossip = {str(gossipID): {'action': action, 'confidant': confidant,'sensationalism':sensationalism, 'trust': trust}}
		# use the source name as key update spreader
		citizen_list[spreader['name']]['knownRumours'].update(subjectiveGossip)



	# THE SPREADER KNOWS WHO THEY SPREAD IT TO
	if type=='spread':
		# Update self spread count
		# global updated upon reciept 
		gossipID      = gossipObject['gossipID']
		action        = 'spreaded'
		confidant     = other_citizen['name']
		trust         = random.randint(40,70)

		subjectiveGossip = {str(gossipID): {'action': action, 'confidant': confidant, 'trust': trust}}
		#update spreader 
		citizen_list[spreader['name']]['knownRumours'].update(subjectiveGossip)




	# the reciever knows the source
	if type=='acceptRumour':
		gossipID      = gossipObject['gossipID']
		action        = 'received'
		source        = spreader['name']
		sensationalism = gossipObject['sensationalism']
		trust         = random.randint(0,65)
		subjectiveGossip = {str(gossipID): {'action': action, 'source': source,'sensationalism':sensationalism, 'trust': trust}}
		
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


		# LOGGING
		logReceivedGossip(LOG_DICT["RECEIVE_LOGFILE"],gossipID,spreader['name'],other_citizen['name'],awardedSP,sourceCitizensSP,other_citizen['knownRumours'],citizen_list,rumourTarget,sentiment)
		# Random updates to log
		logUpdateMessage(str(spreader['name'] + ' told ' + str(other_citizen['name']) + ' a rumour. They received ' + str(awardedSP) + ' status points. They had ' + str(sourceCitizensSP) + ' \n'),LOG_DICT["GOSSIP_ACTIONS"])
		logUpdateMessage(str(str(rumourTarget) + ' was gosssiped about, the sentiment was ' + str(sentiment) + ' they had ' + str(tSP) + ' status points. They now have ' + str(citizen_list[rumourTarget]['SP'])+ ' \n' ),LOG_DICT["GOSSIP_ACTIONS"])


		# TODO
		# UPDATE SPREAD COUNT
		gossip_database[gossipID]['spread_count'] = gossip_database[gossipID]['spread_count'] + 1


	return(citizen_list,gossip_database)

#def pickRumour():
	# pick a rumour to spread 

