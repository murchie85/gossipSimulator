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
def stringMod(string,blockLen=50,endChar='|',nospace='no'):
	allowedLen = blockLen - 4 # allow for | 
	difference = allowedLen - len(string)
	# pad with spaces
	if difference > 0:
		for i in range(0, difference):
			string += " "

	if difference < 0:
		string = string[:allowedLen]

	printString = endChar + " " + string + " "  + endChar
	if(nospace=='yes'):
		printString = endChar + string   + endChar
	if(nospace=='right'):
		printString = endChar + " " + string   + endChar
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






def nextDay(game_time,day_len,gossip_database,citizenArray,citizen_list):

	endDay = Art=text2art("End of Day")
	print(endDay)

	spList   = [x['SP'] for x in citizenArray]
	maxSP    = max(spList)
	arrIndex = spList.index(maxSP)

	printString = ("Top performer: " + str(citizenArray[arrIndex]['name'])  + ' with ' + str(citizenArray[arrIndex]['SP']) + ' SP.' )


	chosen = 'L'

	while((chosen.upper() != 'C') and (chosen!= '') ):
		print('[1] Options')
		print('[2] Insights')
		print('[3] stats')
		print('')
		print('[C] Continue')
		chosen = input('Enter A Value \n')
		if(chosen == '1'):
			print("\033c")
			options()
		if(chosen == '2'):
			print("\033c")
			insights(citizen_list)
			print("\033c")
		if(chosen == '3'):
			print("\033c")
			stats(printString,gossip_database)

	time.sleep(1)	


	return()


def options():
	chosen = 999999999999
	selectedOption = 99
	
	rulesFile = "rules/RULES.txt"
	rulesList = getAllRuleNames(rulesFile)
	
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

		if((selectedOption >=0) and selectedOption < (len(rulesList))): break


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





def insights(citizen_list):
	print("\033c")


	chosenIndex = 0
	pa1 = []
	pa2 = []
	pa3 = []
	pa4 = []
	pa5 = []
	pa6 = []
	pa7 = []
	pa8 = []
	pa9 = []
	pa10 = []
	pa11 = []
	pa12 = []

	for x in range(len(citizen_list)):
		# extract dict items
		key = list(citizen_list.keys())[chosenIndex]
		index = citizen_list[key]
		created, received = 0,0
		for rumour in index['knownRumours']:
			action = index['knownRumours'][rumour]['action']
			if('created' in action): created +=1
			if('received' in action): received +=1 

		pa1.append(stringMod(str('----------------------------------'),blockLen=34,endChar='-',nospace='yes'))
		pa2.append(stringMod(str('    ' + str(index['name'])),blockLen=34,endChar='|',nospace='right'))
		pa3.append(stringMod(str('---------------------------------'),blockLen=34,endChar='-',nospace='yes'))
		pa4.append(stringMod(str(''),blockLen=34,nospace='right'))
		pa5.append(stringMod(str('Create Gossip Chance: ' + str(index['CGP'])),blockLen=34,nospace='right'))
		pa6.append(stringMod(str('Spread Gossip Chance: ' + str(index['SGP'])),blockLen=34,nospace='right'))
		pa7.append(stringMod(str('Status points       : ' + str(index['SP'])),blockLen=34,nospace='right'))
		pa8.append(stringMod(str('Age                 : ' + str(index['age'])),blockLen=34,nospace='right'))
		pa9.append(stringMod(str('Known Rumours       : ' + str(len(index['knownRumours']))),blockLen=34,nospace='right'))
		pa10.append(stringMod(str('Created             : ' + str(created)),blockLen=34,nospace='right'))
		pa11.append(stringMod(str('Received            : ' + str(received)),blockLen=34,nospace='right'))
		pa12.append(stringMod(str('---------------------------------'),blockLen=34,endChar='-',nospace='yes'))
		chosenIndex+=1

	noCitizens=len(citizen_list)
	print("\033c")
	print('*************************************************************************************************************************************************************')
	for x in range(20):print('')
	for i in range(0,noCitizens, 4):
		a,b,c=1,2,3
		if(i+a>=noCitizens): a=0
		if(i+b>=noCitizens): b=0
		if(i+c>=noCitizens): c=0

		print(str(pa1[i]) + ' ' + str(pa1[i+a]) + ' ' + str(pa1[i+b]) + ' ' + str(pa1[i+c]))
		print(str(pa2[i]) + ' ' + str(pa2[i+a]) + ' ' + str(pa2[i+b]) + ' ' + str(pa2[i+c]))
		print(str(pa3[i]) + ' ' + str(pa3[i+a]) + ' ' + str(pa3[i+b]) + ' ' + str(pa3[i+c]))
		print(str(pa4[i]) + ' ' + str(pa4[i+a]) + ' ' + str(pa4[i+b]) + ' ' + str(pa4[i+c]))
		print(str(pa5[i]) + ' ' + str(pa5[i+a]) + ' ' + str(pa5[i+b]) + ' ' + str(pa5[i+c]))
		print(str(pa6[i]) + ' ' + str(pa6[i+a]) + ' ' + str(pa6[i+b]) + ' ' + str(pa6[i+c]))
		print(str(pa7[i]) + ' ' + str(pa7[i+a]) + ' ' + str(pa7[i+b]) + ' ' + str(pa7[i+c]))
		print(str(pa8[i]) + ' ' + str(pa8[i+a]) + ' ' + str(pa8[i+b]) + ' ' + str(pa8[i+c]))
		print(str(pa9[i]) + ' ' + str(pa9[i+a]) + ' ' + str(pa9[i+b]) + ' ' + str(pa9[i+c]))
		print(str(pa10[i]) + ' ' + str(pa10[i+a]) + ' ' + str(pa10[i+b]) + ' ' + str(pa10[i+c]))
		print(str(pa11[i]) + ' ' + str(pa11[i+a]) + ' ' + str(pa11[i+b]) + ' ' + str(pa11[i+c]))
		print(str(pa12[i]) + ' ' + str(pa12[i+a]) + ' ' + str(pa12[i+b]) + ' ' + str(pa12[i+c]))

	print('')
	input('press any key to continue \n')
	print("\033c")


	return()


def stats(printString,gossip_database):
	print("\033c")
	print(printString)
	print('')

	for key in gossip_database:
		print('Rumour: ' + str(gossip_database[key]['rumour']))
		print('Target: ' + str(gossip_database[key]['target'])  + ' Creator: ' + str(gossip_database[key]['creator']) )
		print('SpreadCount: ' + str(gossip_database[key]['spread_count']) + ' Sentiment: ' + str(gossip_database[key]['sentiment']) + ' Sensationalism: ' + str(gossip_database[key]['sensationalism']) + ' persistence: ' + str(gossip_database[key]['persistence']) + ' status: ' + str(gossip_database[key]['status']) ) 
		print('	')
	print("Number of Rumours: " + str(len(gossip_database)))
	print('')
	input('press any key to continue \n')
	print("\033c")


def insightsOld(printString,citizen_list):
	print("\033c")
	print(printString)
	print('')

	choice =''
	chosenIndex = 0
	while(choice.upper()!='X'):
		# extract dict items
		key = list(citizen_list.keys())[chosenIndex]
		index = citizen_list[key]
		created, received = 0,0
		for rumour in index['knownRumours']:
			action = index['knownRumours'][rumour]['action']
			if('created' in action): created +=1
			if('received' in action): received +=1 


		print('--------------------------------')
		print('    ' + str(index['name']))
		print('--------------------------------')
		print('')
		print('Create Gossip Chance: ' + str(index['CGP']))
		print('Spread Gossip Chance: ' + str(index['SGP']))
		print('Status points       : ' + str(index['SP']))
		print('Age                 : ' + str(index['age']))
		print('Known Rumours       : ' + str(len(index['knownRumours'])))
		print('Created             : ' + str(created))
		print('Received            : ' + str(received))


		print('')
		print('')
		print('[N] Next')
		print('[P] Previous')
		print('[X] Exit')

		choice = input('Select an option. \n')
		if(choice.upper() == 'N'): chosenIndex+=1
		if(choice.upper() == 'P'): chosenIndex-=1
		if(chosenIndex > len(citizen_list)-1): chosenIndex = 0
		if(chosenIndex <0): chosenIndex = len(citizen_list) -1
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

