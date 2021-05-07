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
"""


import random 
from .logging import *



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

	sentiment           = random.randint(0,100)

	# pull in some random gossip, this checks the size ot make sure we don't get empty string
	f = open(gossip_file)
	gossip =""
	gossipArray = f.read().split(';')
	while len(gossip) < 1:
		gossip              = random.choice(gossipArray)

	rumour              = gossip.replace('NAME', str(target))
	risk                = random.randint(0,100)
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
	'spread_count': spread_count,
	'associated_citizens':  associated_citizens,
	}

	gossip_database.update({str(gossipID): gossipObject})

	return(gossip_database, gossipObject)






def updateKnownRumours(citizen_list,spreader, receivingAudience,gossipObject,gossip_database, type,LOG_DICT):

	## THIS UPDATES THE CHARACTERS REFERENCE ONLY
	## ITS SUBJECTIVE BASED UPON THE ACTION

	# THE CREATOR KNOWS HE/SHE CREATED IT
	if type=='create':
		gossipID      = gossipObject['gossipID']
		action        = 'created'
		confidant     = receivingAudience['name']
		trust         = 100

		subjectiveGossip = {str(gossipID): {'action': action, 'confidant': confidant, 'trust': trust}}
		# use the source name as key update spreader
		citizen_list[spreader['name']]['knownRumours'].update(subjectiveGossip)



	# THE SPREADER KNOWS WHO THEY SPREAD IT TO
	if type=='spread':
		gossipID      = gossipObject['gossipID']
		action        = 'spreaded'
		confidant     = receivingAudience['name']
		trust         = random.randint(40,70)

		subjectiveGossip = {str(gossipID): {'action': action, 'confidant': confidant, 'trust': trust}}
		#update spreader 
		citizen_list[spreader['name']]['knownRumours'].update(subjectiveGossip)


	# the reciever knows the source
	if type=='acceptRumour':
		gossipID      = gossipObject['gossipID']
		action        = 'received'
		source        = spreader['name']
		trust         = random.randint(0,65)
		subjectiveGossip = {str(gossipID): {'action': action, 'source': source, 'trust': trust}}
		# update reciever 
		citizen_list[receivingAudience['name']]['knownRumours'].update(subjectiveGossip)

		# award status points
		targetCitizensSP = citizen_list[spreader['name']]['SP']
		awardedSP        = round((1/random.randint(1,9)) * trust) # a fraction of trust
		totalSP          = targetCitizensSP + awardedSP 

		rumourTarget    = gossipObject['target']
		sentiment       = gossipObject['sentiment']
		
		#print(citizen_list[spreader['name']]['SP'])
		citizen_list[spreader['name']]['SP'] = totalSP


		logReceivedGossip(LOG_DICT["RECEIVE_LOGFILE"],gossipID,spreader['name'],receivingAudience['name'],awardedSP,targetCitizensSP,receivingAudience['knownRumours'],citizen_list,rumourTarget,sentiment)
		# Random updates to log
		logUpdateMessage(str(spreader['name'] + ' told ' + str(receivingAudience['name']) + ' a rumour. They reveived ' + str(awardedSP) + ' status points. They had ' + str(targetCitizensSP) + ' \n'),LOG_DICT["GOSSIP_ACTIONS"])


		# TODO
		# UPDATE SPREAD COUNT
		# MIGRATE THIS LATER TO SPREAD 
		gossip_database[gossipID]['spread_count'] = gossip_database[gossipID]['spread_count'] + 1







	return(citizen_list,gossip_database)



