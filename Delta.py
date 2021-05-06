import difflib 

#gameFileA
gameFile = '/Users/adammcmurchie/2021/fishwives/game/functions/botDecisionTree.py'
gameFileA = '/game/functions/rules.py'
gameFile = '/game/functions/processGossip.py'
gameFile = '/game/functions/create_citizen.py'

#DOSFileA
DOSFILE = '/Users/adammcmurchie/2021/fishwives/DOS/functions/botDecisionTree.py'
DOSFileA = 'DOS/functions/rules.py'
DOSFILE = 'DOS/functions/processGossip.py'
DOSFILE = 'DOS/functions/create_citizen.py'


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