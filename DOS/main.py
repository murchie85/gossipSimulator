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
from functions.utils import *
from functions.draw import *
from functions.processGossip import *  
from functions.botDecisionTree import * 
import time
import os
if os.path.exists("logs/gossip.txt"):os.remove("logs/gossip.txt")

#**************************************  
#    ---------SIM VARIABLES  -----  
#*************************************** 

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
startMesssage(citizen_count,citizen_list,'no')
# time buffered by sleep
# This clears the screen
print("\033c")
## This loops until it gets the a full month
for i in range(0, month_len):
	citizenArray = []
	game_time     +=1
	for key in citizen_list: citizenArray.append(citizen_list[key])



	#************************************************************************************
	#
	#              ---------------BOT ACTIONS---------------                          *
	#
	#************************************************************************************


	# Loop Citizens 
	# TODO: Randomise this order once MVP done
	for key in citizen_list:
		citizen                        = citizen_list[key]
		position                       = citizen['location']
		citizen_list                   = insertEmoji(citizen,citizen_list,citizen_count)
		gossipObject                   = {} # flush every time 
		# later can make actins all within personality functions  

		#  ------WALK------
		citizen_list[key]['location']  = processMovement(citizen,position)


		# ------CREATE GOSSIP & UPDATE KNOWN RUMOURS------
		citizen,citizen_list,gossip_database,gossipObject = gossipDecision(citizen,citizen_list,key,gossip_database,gossip_file,gossipObject,position)


		# UPATES
		if (len(gossipObject) > 0): gossipUpdates.append(gossipObject)



			



















	#************************************************************************************
	#
	#              ---------------PRINT PRINT---------------                          *
	#
	#************************************************************************************

	##---------------printing first, so updates wont be captured until next round
	drawHeader(game_time,day_len,gossip_database)
	# Add in happy/sad emoji based on status array
	printCitizen(citizenArray)
	print(' ')
	
	#-------top print block------

	# ------UPDATE NOTIFICATION TIMER 
	noticationStatus,messageTime = printNotification(message, messageTime)
	if(noticationStatus != "running"):
		print('length gossip DB: ' + str(len(gossip_database)))

	# PRINT A NOTIFICATION
	if((len(gossipUpdates) > 0)):
		if(noticationStatus == "free"):
			choice = random.choice(['gossip','log'])

			if(choice == 'gossip'):
				chosenGossip = random.choice(gossipUpdates)
				message = '😲😲**new gossip**😲😲 \n' + str(chosenGossip['creator']) + " : " + str(chosenGossip['rumour'])
				messageTime = 5
				gossipUpdates = []
			else:
				with open('logs/gossip.txt', 'r') as f:
				    lines = f.read().splitlines()
				    last_line = lines[-1]
				    message = str(' 😃 Gossip News 😃 ') +  last_line
				    messageTime = 5
				    gossipUpdates = []
				    f.close()


	
	time.sleep(0.5)	
	# This clears the screen
	print("\033c")





