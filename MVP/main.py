from functions.create_citizen import *
from functions.utils import med_print
from functions.printer import *
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
	game_time +=1

	citizenArray = []
	for key in citizen_list:
		citizenArray.append(citizen_list[key])

	printCitizen(citizenArray)



	time.sleep(time_increment)
	print("\033c")


