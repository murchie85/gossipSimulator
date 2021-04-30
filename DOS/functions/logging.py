import csv
from datetime import datetime

def init_files():
	with open('logs/recieve-gossip.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['Time','ID','Spreader','Audience','SP','Originalsp','AudienceKnownRumours','TotalRumours'])




def logReceivedGossip(file,gossipID,spreader,audience,awardedSP,targetCitizensSP,receivingAudienceKnownRumours,citizen_list):
	now = datetime.now() 
	date_time = now.strftime("%m/%d/%Y %H:%M:%S")

	# get total rumour count
	for key in citizen_list: kt = sum(len(x['knownRumours']) for x in citizen_list.values() if x)


	#'time,key,id,spreader,audience,sp,originalsp,audienceKnownRumours,totalRumours,'
	with open(file, 'a', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([str(date_time),str(gossipID),spreader,audience,str(awardedSP),str(targetCitizensSP),str(len(receivingAudienceKnownRumours)),kt])


def logUpdateMessage(message,file):
	f = open(file, 'a')
	f.write(message)
	f.close()