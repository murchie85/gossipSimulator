

def limitGossipWithSamePerson(thisCitizen,other_citizen):
		krLen = len(thisCitizen['knownRumours'])
		if(krLen>0):
			rumourKeys = list(map(int,list(thisCitizen['knownRumours'].keys())))
			rumourKeys.sort()

			## DON'T CREATE GOSSIP TO THE SAME PERSON YOU JUST CREATED TO 
			gosIndex = 1
			for x in range(1,krLen):
				if(('confidant' in thisCitizen['knownRumours'][str(rumourKeys[-x])]) ):
					gosIndex = x
					break

			if('confidant' in thisCitizen['knownRumours'][str(rumourKeys[-gosIndex])]):
				if(other_citizen['name'] == thisCitizen['knownRumours'][str(rumourKeys[-gosIndex])]['confidant']):
					return("False")

		return('True')

def gossipTimeInterval():
		if(('gossiping' in str(citizen['action'])) or ('receiving' in str(citizen['action']))): 
			return(citizen,citizen_list,gossip_database,gossipObject)






## PULL RULES INFO


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

def updateRule(rulesFile,targetVar,targetVal):
	f = open(rulesFile, "r")
	rules = f.read()
	rules = rules.split(',')
	f.close()

	newRules = ""
	for rule in rules:
		if(str(targetVar) in str(rule)):
			updatedRule = str(rule.split(':')[0]) + ":" + str(targetVal)
			newRules+= str(updatedRule) + ','
		else:
			newRules+=str(rule) + ','

	# remove trailing comma
	newRules = newRules[:-1]


	f = open(rulesFile, "w")
	f.write(newRules)
	f.close()


def getAllRuleNames(rulesFile):
	f = open(rulesFile, "r")
	rules = f.read()
	rules = rules.split(',')
	rulesList = []
	for r in rules: 
		rulesList.append(str(r.split(':')[0]))
	return(rulesList)

def getFullRules(rulesFile,targetVar):
	f = open(rulesFile, "r")
	rules = f.read()
	rules = rules.split(',')
	for r in rules: 
		if(r.split(':')[0] == str(targetVar)):
			return(r)

	print('Target variable not found in rules file')
	print('variable is: ' + str(targetVar))
	exit()

def getRulesSchema(rulesFile,targetVar):
	f = open(rulesFile, "r")
	rules = f.read()
	rules = rules.split(';')
	for r in rules: 
		if(r.split(':')[0] == str(targetVar)):
			return(r)

	print('Target variable not found in rules file')
	print('variable is: ' + str(targetVar))
	exit()