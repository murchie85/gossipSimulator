import names 
import time
def createCitizen():
	name = str(names.get_first_name() + names.get_last_name())

	citizen = {"name": name}
	return(citizen)



for citizen in range(0,10):
	print('Creating Citizen')
	citizen = createCitizen()

	print("The Full Citizen Object is : ")
	print(citizen)  
	print(' ')  
	print("Citizen name is {}".format(citizen['name']))
	print(' ')
	time.sleep(1)