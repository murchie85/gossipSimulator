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


import names 
import random



## To be used later to prevent drift
def catalogue():
	terms = {"name": 'STRING This is the ID of the citizen. It is also uses as a primary key for searching. ', 
	"SP": 'INT status points a counter for each citizen, this is valuable like money. ', 
	"CGP": 'INT value from 0 to 100, this is the probability a citizen will start gossip'}

	return(terms)



def createCitizen():
	name            = str(names.get_first_name() + ' ' + names.get_last_name())
	location        = random.randint(0,1000)
	sp              = random.randint(0,100)
	cgp             = random.randint(0,100)
	sgp             = random.randint(0,100)
	age             = random.randint(0,80)
	friends         = {}
	knownRumours    = {}
	emotion         = '😐'

	citizen = {"name": name, "location": location, "SP": sp, "CGP": cgp, "SGP": sgp, "age": age, "friends": friends, "knownRumours": knownRumours, 'emotion':emotion}
	return(citizen)


def generateCitizens(citizen_count):

	citizen_list  = {}

	for citizen in range(0,citizen_count):
		print('----------------')
		print('Creating Citizen')
		print('----------------')
		citizen = createCitizen()
		citizen_list.update({ str(citizen['name']): citizen})

		print("The Full Citizen Object is : ")
		print(citizen)  
		print(' ')  

		print("Citizen name is {}".format(citizen['name']))
		print(' ')

		print("Citizen's age is {}".format(citizen['age']))
		print(' ')

		print("Citizen's location is {}".format(citizen['location']))
		print(' ')

		print("Citizen's status points are {}".format(citizen['SP']))
		print(' ')

		print("Citizen's create gossip probability is {}".format(citizen['CGP']))
		print(' ')

		print("Citizen's spread gossip probability is {}".format(citizen['SGP']))
		print(' ')

		print("Citizen's friends are {}".format(citizen['friends']))
		print(' ')

		print("Citizen's known rumours are {}".format(citizen['knownRumours']))
		print(' ')  
		#time.sleep(1)

	return(citizen_list)



