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
from functions._DOS_printer import *

from functions.processCitizen import *
from functions.utils import *
from functions.processGossip import *  
from functions.botDecisionTree import * 
from functions.logging import *
import time
import random
import os
import pprint


#LOGS_gossip_actions
GOSSIP_LOGFILE        = "logs/LOGS_gossip.txt"
GOSSIP_ACTIONS        = "logs/LOGS_gossip_actions.txt"
RECEIVE_LOGFILE       = "logs/LOGS_recieved-gossip.csv"

DATABASE_CITIZENLIST  = "logs/DATABASE_CitizensList.txt"
DATABASE_GOSSIP       = "logs/DATABASE_Gossip.txt"
LOG_DICT ={"GOSSIP_LOGFILE":GOSSIP_LOGFILE,"GOSSIP_ACTIONS":GOSSIP_ACTIONS,"RECEIVE_LOGFILE": RECEIVE_LOGFILE, "DATABASE_CITIZENLIST": DATABASE_CITIZENLIST,"DATABASE_GOSSIP":DATABASE_GOSSIP}

if os.path.exists(GOSSIP_LOGFILE):os.remove(GOSSIP_LOGFILE)
if os.path.exists(GOSSIP_ACTIONS):os.remove(GOSSIP_ACTIONS)
if os.path.exists(RECEIVE_LOGFILE):os.remove(RECEIVE_LOGFILE)
if os.path.exists(DATABASE_CITIZENLIST):os.remove(DATABASE_CITIZENLIST)
if os.path.exists(DATABASE_GOSSIP):os.remove(DATABASE_GOSSIP)


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
gossip_file = "gossip/gossipDict.txt"

#--------------------
## DATABASE CREATION 
#--------------------
citizen_list = generateCitizens(15)
gossip_database = {}
chosenGossip = ""

#----------------
# DOS 
#----------------
gameSpeed = int(getRules("rules/RULES.txt",'gameSpeed'))


# Print start 
init_files(RECEIVE_LOGFILE)
# set to yes to skip intro
startMesssage(citizen_count,citizen_list,'yes')
# TODO: makes this Universal so a library of settings can be picked
#defaultSettings()



# clear screen
print("\033c")

## This loops until it gets the a full month
for i in range(0, month_len):
	citizenArray = []
	game_time     +=1
	gameSpeed = int(getRules("rules/RULES.txt",'gameSpeed'))

	for key in citizen_list: citizenArray.append(citizen_list[key])



	#************************************************************************************
	#
	#              ---------------BOT ACTIONS---------------                          *
	#
	#************************************************************************************


	# Loop Citizens 
	# TODO: Randomise this order once MVP done
	# TODO: Pretty print
	for key in citizen_list:
		citizen                        = citizen_list[key]
		position                       = citizen['location']
		citizen_list                   = processEmotion(citizen,citizen_list,citizen_count)
		gossipObject                   = {} # flush every time 
		# later can make actins all within personality functions  

		#  ------WALK------
		citizen_list[key]['location']  = processMovement(citizen,position)


		# ------CREATE GOSSIP & UPDATE KNOWN RUMOURS------
		citizen,citizen_list,gossip_database,gossipObject = gossipDecision(citizen,citizen_list,key,gossip_database,gossip_file,gossipObject,position,LOG_DICT)


		# Print Gossip bubble
		citizenAction = citizen['action']
		if(len(citizenAction) > 0):
			if((citizenAction[0] == 'gossiping') or (citizenAction[0] == 'receiving') ):
				citizenAction[1] = (citizenAction[1] -1)
				# reset once it hits 0
				if(citizenAction[1] <1):
					citizen['action'] = []


		# UPATES
		if (len(gossipObject) > 0): gossipUpdates.append(gossipObject)

	# END CITIZEN LOOP
	gossip_database,citizen_list = reducePersistence(gossip_database,citizen_list,LOG_DICT)

	#************************************************************************************
	#
	#              ---------------PRINT PRINT---------------                          *
	#
	#************************************************************************************

	##---------------printing first, so updates wont be captured until next round
	drawHeader(game_time,day_len,gossip_database,gameSpeed)
	# Add in happy/sad emoji based on status array
	printCitizen(citizenArray)
	print(' ')

	#-------top print block------


	#************************************************************************************
	#
	#              ---------------NOTIFICATION AND LOGGING---------------                          *
	#
	#************************************************************************************


	# ------UPDATE NOTIFICATION TIMER 
	noticationStatus,messageTime = printNotification(message, messageTime)
	if(noticationStatus != "running"):
		print('length gossip DB: ' + str(len(gossip_database)))

	# Choses a random gossip string to write, skips if no new updates
	chosenGossip = logRandomUpdate(gossipUpdates,chosenGossip,LOG_DICT['GOSSIP_LOGFILE'])

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
				with open(GOSSIP_ACTIONS, 'r') as f:
				    lines = f.read().splitlines()
				    last_line = lines[-1]
				    message = str(' 😃 Gossip News 😃 ') +  last_line
				    messageTime = 5
				    gossipUpdates = []
				    f.close()


	# Save latest data structure
	pout = pprint.pformat(citizen_list, indent=4)
	logUpdateMessage(pout,DATABASE_CITIZENLIST,'w')

	# Save latest Gossip data structure
	pout = pprint.pformat(gossip_database, indent=4)
	logUpdateMessage(pout,DATABASE_GOSSIP,'w')


	# NEXT DAY 	
	if(game_time%day_len ==0):
		nextDay(game_time,day_len,gossip_database,citizenArray,citizen_list)



	time.sleep(1/gameSpeed)	
	# This clears the screen
	print("\033c")





