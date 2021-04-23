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
import time
import random
from utils import med_print


## To be used later to prevent drift
def catalogue():
	terms = {"name": 'STRING This is the ID of the citizen. It is also uses as a primary key for searching. ', 
	"SP": 'INT status points a counter for each citizen, this is valuable like money. ', 
	"CGP": 'INT value from 0 to 100, this is the probability a citizen will start gossip'}

	return(terms)



def createCitizen():
	name            = str(names.get_first_name() + names.get_last_name())
	sp              = random.randint(0,100)
	cgp             = random.randint(0,100)
	sgp             = random.randint(0,100)
	age             = random.randint(0,80)
	friends         = {}
	knownRumours    = {}

	citizen = {"name": name, "SP": sp, "CGP": cgp, "SGP": sgp, "age": age, "friends": friends, "knownRumours": knownRumours}
	return(citizen)



med_print('Generating World...')

citizen_count = 15

for citizen in range(0,citizen_count):
	print('----------------')
	print('Creating Citizen')
	print('----------------')
	citizen = createCitizen()

	print("The Full Citizen Object is : ")
	print(citizen)  
	print(' ')  

	print("Citizen name is {}".format(citizen['name']))
	print(' ')

	print("Citizen's age is {}".format(citizen['age']))
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

	time.sleep(1)

print("\033c")
print('************************************************')
print('    😏😏😏  GOSSIP SIMULATOR      😏😏😏       ')
print('************************************************') 
print('')
med_print("World Complete")
print(' ')
med_print('Number of Citizens: ' + str(citizen_count))
print('')
print('')
input('Press any button to begin simulation')