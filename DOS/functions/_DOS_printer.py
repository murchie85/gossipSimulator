"""

This function prints row of 3 boxed 


"""
import math
import time
from art import *
from .utils import med_print
from .rules import *
from .logging import *
import random
import textwrap as tr

blockLen     = 50
blocksPerRow = 3


def drawHeader(game_time,day_len,gossip_database,speed):
	print('****************************************************************************************************************************************************')
	print('*                                                                                                                                                  *')
	print('*    Welcome to Celestus Town         Day: ' + str(round(game_time/day_len)) + "      time: " + str(game_time)  + '    Gossip Count: ' + str(len(gossip_database))    + '      speed:'  + str(speed))   
	print('*                                                                                                                                                  *')
	print('****************************************************************************************************************************************************')
	

# prints out exactly 50 lines
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
		print( stringMod("Name[" +str(i)     + "] : " + str(citizen[i]['name'] + " " + str(citizen[i]['emotion'])),49) + 
			   stringMod("Name[" +str(i + 1) + "] : "  + str(citizen[i + 1]['name'] + " " + str(citizen[i + 1]['emotion'])),49)  + 
			   stringMod("Name[" +str(i + 2) + "] : "  + str(citizen[i + 2]['name'] + " " + str(citizen[i + 2]['emotion'])),49) 
			   )
		
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
def startMesssage(citizen_count,citizen_list,skip='no'):
	if(skip=='yes'):
		return
	print("\033c")
	print('Generating World...')
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
	time.sleep(1.5)
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




def defaultSettings():
	# GET RULES FROM FILE 
	rulesFile = "rules/RULES.txt"
	gossipStimulation = getFullRules(rulesFile,'gossipStimulation')
	talkingDistance   = getFullRules(rulesFile, 'talkingDistance')
	luckyChance       = getFullRules(rulesFile,'luckyChance')
	rulesArray = [gossipStimulation,talkingDistance,luckyChance]
	ruleDescFile = "rules/rules_schema.txt"
	
	rulesDesc  = [str(getRulesSchema(ruleDescFile,'gossipStimulation')),
				  str(getRulesSchema(ruleDescFile,'talkingDistance')),
				  str(getRulesSchema(ruleDescFile,'luckyChance'))]


	#chosenRule = str(rulesArray[ruleSelected].split(':')[0])
	#ruleValue  = str(rulesArray[ruleSelected].split(':')[1])

	print("\033c")
	for x in range(0,len(rulesArray)):
		print(rulesArray[x])
		print(rulesDesc[x])






def nextDay(game_time,day_len,gossip_database,citizenArray):

	endDay = Art=text2art("End of Day")
	print(endDay)

	spList   = [x['SP'] for x in citizenArray]
	maxSP    = max(spList)
	arrIndex = spList.index(maxSP)

	printString = ("Top performer: " + str(citizenArray[arrIndex]['name'])  + ' with ' + str(citizenArray[arrIndex]['SP']) + ' SP.' )


	chosen = ''

	while(chosen != 'x'):
		print('[1] Options')
		print('[2] Insights')
		print('')
		print('[x] Exit')
		chosen = input('Enter A Value \n')
		if(chosen == '1'):
			options()
		if(chosen == '2'):
			insights(printString)

	time.sleep(1)	


	return()


def options():
	chosen = 999999999999
	selectedOption = 99
	
	rulesFile = "rules/RULES.txt"
	rulesList = ['gossipStimulation','talkingDistance','luckyChance','gameSpeed','citizenWalkSpeed']
	
	while(isinstance(selectedOption, int)):
		print("\033c")
		print('Select a value to Modify')
		for x in range(0, len(rulesList)):
			print('[' + str(x) + '] ' + str(rulesList[x]))

		print('[x] Exit')
		print('')
		selectedOption = input('Enter a value. \n')

		# if x exit, if num continue, else retry
		try:
			selectedOption = int(selectedOption)
		except: 	
			if(str(selectedOption) =='x'):
				print("\033c")
				return()
			else:
				 print('Please pick an integer between 1-20  ' + str(selectedOption))
				 selectedOption = 99

		if((selectedOption >=0) and selectedOption < (len(rulesList) -1)): break


	while(isinstance(chosen, int)):
		RuleName  = rulesList[selectedOption]
		ruleValue = int(getRules("rules/RULES.txt",str(RuleName)))
		ruleInfo  = getRulesSchema("rules/rules_schema.txt",RuleName)
		ruleInfo = str(str(ruleInfo).split(':')[1]).strip('[]')

		print("\033c")
		print(str(RuleName) + ': ' + str(ruleValue))
		print('')
		print(tr.fill(ruleInfo,35))
		print('')

		print('[x] Exit')
		print('')

		
		chosen = input('Enter a value. \n')
		try:
			chosen = int(chosen)
		except: 	
			if(str(chosen) =='x'):
				print("\033c")
				return()
			else:
				 print('Please pick an integer between 1-20  ' + str(chosen))
				 chosen = 999999999999

		if((chosen >=0) and chosen < 9999999): 
			updateRule(rulesFile,RuleName,chosen)
			print("\033c")
			RuleName  = rulesList[selectedOption]
			ruleValue = int(getRules("rules/RULES.txt",str(RuleName)))
			print(str(RuleName) + ': ' + str(ruleValue))
			print('')
			print('***UDPATED**')
			time.sleep(1.5)
			print("\033c")
			return()


	return()



def insights(printString):
	print("\033c")
	print(printString)
	print('')
	input('Pressy return to continue. ')
	print("\033c")


	return()

#------------------------------------------------------------------------------------------------------
#
#                             Common 
#
#------------------------------------------------------------------------------------------------------

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

def logRandomUpdate(gossipUpdates,chosenGossip,filePath):
	if((len(gossipUpdates) > 0 )):
		oldGossip    = chosenGossip	
		if(oldGossip in gossipUpdates):
			return(chosenGossip)
		else:
			chosenGossip = random.choice(gossipUpdates)
			um = str('New Gossip: ' + str(chosenGossip['creator']) + " : " + str(chosenGossip['rumour'] + '\n'))
			logUpdateMessage(um,filePath)

	return(chosenGossip)

