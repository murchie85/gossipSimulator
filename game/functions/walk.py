import random

def moveCitizen(citizen,position):

	stepValue = random.randint(-10,10)

	# occasionally stop
	chance = random.randint(0,4)
	if(chance == 2): stepValue = 0

	newPosition = position + stepValue

	if newPosition > 1000: 
		newPosition = newPosition - 1000
		
	if newPosition < 0: newPosition = 1000 - newPosition


	return(newPosition)
