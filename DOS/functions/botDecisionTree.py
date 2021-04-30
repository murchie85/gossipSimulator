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
		other_citizen_position    = other_citizen['location']
		distanceApart = getDistanceApart(myPosition,other_citizen_position,thisCitizen,other_citizen)




		# RANDOM CHANCE
		createGossipProbability = thisCitizen['CGP']
		gossipStimulation = getRules("rules.txt",'gossipStimulation')
		chance = random.randint(1,int(gossipStimulation))
		myChance = createGossipProbability + chance

		luckyChance = random.randint(0,10000)



		# CREATE AND SPREAD GOSSIP
		if((myChance > 90) and (distanceApart < 10) or (luckyChance == 10)):
			#print(str(thisCitizen['name']) + ' and ' + str(other_citizen['name']) + ' are within ' + str(distanceApart) + ' of each other and about to gossip.')
			#print(str(thisCitizen['name']) + ' cgp= ' + str(createGossipProbability) + ' chance= ' + str(chance) )
			#print('lucky chance = ' + str(luckyChance))

			# Creates a gossip object
			gossip_database, gossipObject = createRumour(gossip_database, citizen_list, creator=citizen['name'], gossip_file=gossip_file)  
			
			# updates the fishwifes internal reference
			citizen_list = updateKnownRumours(citizen_list,citizen, other_citizen ,gossipObject, 'create')

			# Reciever accepts rumour (at a given trust value)
			citizen_list = updateKnownRumours(citizen_list,citizen, other_citizen ,gossipObject, 'acceptRumour')




	return(citizen,citizen_list,gossip_database,gossipObject)


def getDistanceApart(myPosition,other_citizen_position,thisCitizen,other_citizen):
	distanceApart             = abs(myPosition - other_citizen_position)

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
	
	