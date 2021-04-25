"""

This function prints row of 3 boxed 


"""
import math
import time
from art import *
from .utils import med_print

blockLen     = 50
blocksPerRow = 3

def stringMod(string,blockLen=50):
	allowedLen = blockLen - 4 # allow for | 
	difference = allowedLen - len(string)
	# pad with spaces
	if difference > 0:
		for i in range(0, difference):
			string += " "

	if difference < 0:
		string = string[:allowedLen]

	printString = "| " + string + " |"
	return(printString)

def printCitizen(citizen):
	iterations = math.floor(len(citizen)/blocksPerRow)
	print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
	for i in range(0, len(citizen), 3):
		print( stringMod("Name[" +str(i) + "] : " + str(citizen[i]['name'])) + 
			   stringMod("Name[" +str(i + 1) + "] : "  + str(citizen[i + 1]['name']))  + 
			   stringMod("Name[" +str(i + 2) + "] : "  + str(citizen[i + 2]['name']))     )
		
		print( stringMod("Location: " + str(citizen[i]['location'])) + 
			   stringMod("Location: " + str(citizen[i + 1]['location']))  + 
			   stringMod("Location: " + str(citizen[i + 2]['location']))     )
		
		print( stringMod("Status Points: " + str(citizen[i]['SP'])) + 
			   stringMod("Status Points: " + str(citizen[i + 1]['SP']))  + 
			   stringMod("Status Points: " + str(citizen[i + 2]['SP']))     )
		
		print( stringMod("Known Rumours: " + str(len(citizen[i]['knownRumours']))) + 
			   stringMod("Known Rumours: " + str(len(citizen[i + 1]['knownRumours'])))  + 
			   stringMod("Known Rumours: " + str(len(citizen[i + 2]['knownRumours']))) )

		print("-------------------------------------------------------------------------------------------------------------------------------------------------------")



#------------PRINT FUNCTIONS -----------------
def startMesssage(citizen_count,citizen_list):
	print("\033c")
	med_print('Generating World...')
	print("\033c")
	print('************************************************')
	print('    😏😏😏  GOSSIP SIMULATOR      😏😏😏       ')
	print('************************************************') 
	print('')
	print("World Complete")
	print(' ')
	print('Number of Citizens: ' + str(citizen_count))
	print('')
	print('')
	print(citizen_list)
	#input('Press any button to begin simulation')
	print("\033c")
	print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
	starting  =text2art("                                              Starting") 
	simulation=text2art("                                              Simulation") 

	print(starting)
	print('')
	print(simulation)
	time.sleep(3)
	print("\033c")
	three=text2art("                                                                  3") 
	two  =text2art("                                                                  2") 
	one  =text2art("                                                                  1") 
	start  =text2art("                                                   start") 

	print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
	print(three)
	time.sleep(1)
	print("\033c")

	print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
	print(two)
	time.sleep(1)
	print("\033c")

	print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
	print(one)
	time.sleep(1)
	print("\033c")

	print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
	print(start)
	time.sleep(1)
	print("\033c")



#  this will print a messages for a given time.
#  it counts down a timer to keep printing message
def printNotification(message, messageTime):
	if message == "":
		return('free',messageTime)

	if messageTime >= 0:
		print(message)
		messageTime -=1
		return('running',messageTime)

	if messageTime < 0:
		return('free',messageTime)