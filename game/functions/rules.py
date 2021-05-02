

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