import difflib 

#gameFileA
gameFile = '/Users/adammcmurchie/2021/fishwives/game/functions/botDecisionTree.py'
gameFile = '/Users/adammcmurchie/2021/fishwives/game/functions/rules.py'
gameFileA = '/Users/adammcmurchie/2021/fishwives/game/functions/processGossip.py'
gameFile = '/Users/adammcmurchie/2021/fishwives/game/functions/create_citizen.py'

#DOSFileA
DOSFILE = '/Users/adammcmurchie/2021/fishwives/DOS/functions/botDecisionTree.py'
DOSFILE = '/Users/adammcmurchie/2021/fishwives/DOS/functions/rules.py'
DOSFileA = '/Users/adammcmurchie/2021/fishwives/DOS/functions/processGossip.py'
DOSFILE = '/Users/adammcmurchie/2021/fishwives/DOS/functions/create_citizen.py'


with open(DOSFileA) as f1:
	f1_text = f1.read()

with open(gameFileA) as f2:
	f2_text = f2.read()

f1_text = f1_text.strip().splitlines()
f2_text = f2_text.strip().splitlines()

# Find and print the diff:
print("Printing the differences Game file has over Dos file: ")
for line in difflib.unified_diff(f1_text, f2_text, fromfile=DOSFileA, tofile=gameFileA, lineterm=''):
	if(line[0] == '+'):
		print(line)