"""
# Program Name: main
# Author: Adam McMurchie
# DOC: 24 April 2021
# Summary: This is the entry function to the program. 
#          This program loops over game_time, each loop
#          functions will be called to update citizen, 
#          make them walk, gossip etc.
#          print functions are used to display progress
# ***********ALL STATE IS STORED HERE******************
#
"""

## Internal libraries
from functions.create_citizen import *
from functions.update_citizen import *
from functions.utils import med_print
from functions.printer import *
from functions.walk import *
from functions.create_gossip import *  

import time

# Set up Time
game_time      = 0
day_len        = 60
month_len      = 28 * day_len
time_increment = 1

# gossip
gossipObject      = ""
gossipUpdates     = []
displayGossipTime = 2

# print vars 
message           = ""
messageTime       = 5

# Citizens
citizen_count = 15

# Files
gossip_file = "gossip/mvpGossip.txt"

#--------------------
## DATABASE CREATION 
#--------------------
citizen_list = generateCitizens(15)
gossip_database = {}




# Print start 
startMesssage(citizen_count,citizen_list)




# This clears the screen
print("\033c")

## This loops until it gets the a full month
for i in range(0, month_len):

	##---------------printing first, so updates wont be captured until next round
	print('********************************************************************************************************************')
	print('*                                                                                                                  *')
	print('*    Welcome to Celestus Town         Day: ' + str(round(game_time/day_len)) + "                                  	  time: " + str(game_time)      )   
	print('*                                                                                                                  *')
	print('********************************************************************************************************************')
	citizenArray = []
	for key in citizen_list: citizenArray.append(citizen_list[key])
	# Add in happy/sad emoji based on status array
	printCitizen(citizenArray)
	print(' ')
	
	#-------top print block------






	noticationStatus,messageTime = printNotification(message, messageTime)
	

	if(noticationStatus != "running"):
		print('length gossip DB: ' + str(len(gossip_database)))

	if((len(gossipUpdates) > 0) and (noticationStatus == "free")):
		chosenGossip = random.choice(gossipUpdates)
		message = '****new gossip*** \n' + str(chosenGossip['creator']) + " : " + str(chosenGossip['rumour'])
		messageTime = 5
		gossipUpdates = []



	# Action will be updated in next print
	game_time     +=1
	

	# Loop Citizens 
	for key in citizen_list:
		citizen                        = citizen_list[key]
		position                       = citizen['location']
		gossipObject                   = {} # flush every time 

		# later can make actins all within personality functions  

		# ACTION:   ------WALK------
		citizen_list[key]['location']  = moveCitizen(citizen,position)

		# ACTION    ------CREATE GOSSIP & UPDATE KNOWN RUMOURS------
		myVar = random.randint(0,100)
		if(myVar == 8):
			gossip_database, gossipObject = createRumour(gossip_database, citizen_list, creator=citizen['name'], gossip_file=gossip_file)  
			citizen_list = updateKnownRumours(citizen_list,key, gossipObject, type='create')
		



		# UPATES
		if (len(gossipObject) > 0): gossipUpdates.append(gossipObject)

	time.sleep(0.5)	
	# This clears the screen
	print("\033c")


