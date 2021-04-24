from functions.create_citizen import *
from functions.utils import med_print
from functions.printer import *
from functions.walk import *
import time

# Set up Time
game_time      = 0
day_len        = 60
month_len      = 28 * day_len
time_increment = 1

# Citizens
citizen_count = 15
citizen_list = generateCitizens(15)









# Print start 
startMesssage(citizen_count,citizen_list)



print("\033c")
for i in range(0, month_len):
	print('********************************************************************************************************************')
	print('*                                                                                                                  *')
	print('*    Welcome to Celestus Town         Day: ' + str(round(game_time/day_len)) + "                                  	  time: " + str(game_time)      )   
	print('*                                                                                                                  *')
	print('********************************************************************************************************************')

	citizenArray = []
	for key in citizen_list: citizenArray.append(citizen_list[key])
	
	# Add in happy/sad emoji based on status array
	printCitizen(citizenArray)
	print(' ')
	# print to debug
	#print(citizenArray)


	# Action will be updated in next print
	game_time +=1
	moveCitizen(citizen_list)



	time.sleep(0.2)
	print("\033c")


