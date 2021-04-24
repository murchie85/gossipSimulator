

def updateKnownRumours(citizen_list,key, gossipObject, type):
	if type=='create':
		gossipID      = gossipObject['gossipID']
		action        = 'created'
		associated    = citizen_list[key]['name']

		subjectiveGossip = {str(gossipID): {'action': action, 'associated': associated}}

		citizen_list[key]['knownRumours'].update(subjectiveGossip)

		return(citizen_list)
