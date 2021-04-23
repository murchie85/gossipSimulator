from functions.create_citizen import *
from functions.utils import med_print
import time

# Set up Time
game_time      = 0
day_len        = 60
month_len      = 28 * day_len
time_increment = 1

# Citizens
citizen_count = 15
citizen_list = generateCitizens(15)




#------------PRINT FUNCTIONS -----------------
med_print('Generating World...')
print("\033c")
print('************************************************')
print('    😏😏😏  GOSSIP SIMULATOR      😏😏😏       ')
print('************************************************') 
print('')
med_print("World Complete")
print(' ')
med_print('Number of Citizens: ' + str(citizen_count))
print('')
print('')
print(citizen_list)
input('Press any button to begin simulation')





# Print Citizen 
def printCitizen(citizen):
	print(str(citizen['name']) + "    Location: " + str(citizen['location']))



print("\033c")
for i in range(0, month_len):
	print('********************************************************************************************************************')
	print('*                                                                                                                  *')
	print('*    Welcome to Celestus Town         Day: ' + str(round(game_time/day_len)) + "                                  	  time: " + str(game_time)      )   
	print('*                                                                                                                  *')
	print('********************************************************************************************************************')
	game_time +=1

	for key in citizen_list:
		printCitizen(citizen_list[key])






	time.sleep(time_increment)
	print("\033c")


