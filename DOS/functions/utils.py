import time
import sys

def med_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)

def insertEmoji(citizen,citizen_list,citizen_count):
	sad = '😢'
	angry = '😡'
	normal = '😐'
	happy='😊'
	excited ='😃'
	sp                             = citizen['SP']
	averageSP                      = (sum(x['SP'] for x in citizen_list.values() if x))/citizen_count

	if(sp<0.30* averageSP):
		citizen_list[citizen['name']]['emotion'] = sad
	if((sp>=0.30* averageSP) and (sp<0.50* averageSP)):
		citizen_list[citizen['name']]['emotion'] = angry
	if((sp>=0.50* averageSP) and (sp<0.60* averageSP)):
		citizen_list[citizen['name']]['emotion'] = normal
	if((sp>=0.60* averageSP) and (sp<0.75* averageSP)):
		citizen_list[citizen['name']]['emotion'] = happy
	if((sp>=0.75* averageSP)):
		citizen_list[citizen['name']]['emotion'] = excited

	return(citizen_list)