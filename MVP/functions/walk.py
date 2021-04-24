import random

def moveCitizen(citizen_list):
	for key in citizen_list:
		citizen  = citizen_list[key]
		position = citizen['location']

		stepValue = random.randint(-10,10)

		# occasionally stop
		chance = random.randint(0,4)
		if(chance == 2): stepValue = 0

		newPosition = position + stepValue

		if newPosition > 1000: 
			newPosition = newPosition - 1000
			
		if newPosition < 0: newPosition = 1000 - newPosition

		citizen['location'] = newPosition

	return(citizen_list)
