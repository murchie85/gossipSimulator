"""
# Program Name: Create_citizen
# Author: Adam McMurchie
# DOC: 23 April 2021
# Summary: This is a function called by main program to create citizens
# This function follows loosely SOLID principles, it creates a citizen only but uses libs to do things like name creation. 


Citizen Initialisation 

- `Id` = uniqueValue (use random name generator so can be in json and prevent duplicates)
- `status_points` = random(0,100)
- `create_gossip_probability` = random int 0-100
- `spread_gossip_probability` = random int 0-100
- `age` = 0
- `friends` = empty
- `subjective_rumour_tracker` empty / knownRumours

"""

import pygame
import names 
import random



## To be used later to prevent drift
def catalogue():
	terms = {"name": 'STRING This is the ID of the citizen. It is also uses as a primary key for searching. ', 
	"SP": 'INT status points a counter for each citizen, this is valuable like money. ', 
	"CGP": 'INT value from 0 to 100, this is the probability a citizen will start gossip'}

	return(terms)



def createCitizen():
	gender          = random.choice(['male','female'])
	name            = str(names.get_full_name(gender=gender))
	location        = [random.randint(0,100),random.randint(0,100)]
	sp              = random.randint(0,100)
	cgp             = random.randint(0,100)
	sgp             = random.randint(0,100)
	age             = random.randint(0,80)
	friends         = {}
	movement        = {}
	knownRumours    = {}
	sprite          = {}
	emotion         = '😐'
	action          = []
	notifyTimer     = random.randint(20,100)

	citizen = {"name": name, "gender":gender, "location": location, "SP": sp, "CGP": cgp, "SGP": sgp, "age": age, "friends": friends, "movement":movement, "knownRumours": knownRumours, "sprite":sprite,'emotion':emotion,"action":action,"notifyTimer":notifyTimer}
	return(citizen)


def generateCitizens(citizen_count):

	citizen_list  = {}

	for citizen in range(0,citizen_count):
		#print('----------------')
		#print('Creating Citizen')
		#print('----------------')
		citizen = createCitizen()
		citizen_list.update({ str(citizen['name']): citizen})  


	return(citizen_list)



def processEmotion(citizen,citizen_list,citizen_count):
	sad     = '1,sad'
	angry   = '2,angry'
	normal  = '3,normal'
	happy   = '4,happy'
	excited = '5,excited'
	sp                             = citizen['SP']
	averageSP                      = (sum(x['SP'] for x in citizen_list.values() if x))/citizen_count

	if(sp<0.30* averageSP):
		citizen_list[citizen['name']]['emotion'] = sad
	if((sp>=0.30* averageSP) and (sp<0.50* averageSP)):
		citizen_list[citizen['name']]['emotion'] = angry
	if((sp>=0.50* averageSP) and (sp<0.60* averageSP)):
		citizen_list[citizen['name']]['emotion'] = normal
	if((sp>=0.60* averageSP) and (sp<0.75* averageSP)):
		citizen_list[citizen['name']]['emotion'] = happy
	if((sp>=0.75* averageSP)):
		citizen_list[citizen['name']]['emotion'] = excited

	return(citizen_list)