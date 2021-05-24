import difflib 

choices = ['botDecisionTree.py','rules.py','processGossip.py','create_citizen.py']

choice = choices[0]

#gameFileA
gameFile= '/Users/adammcmurchie/2021/fishwives/game/functions/' + choice


#DOSFileA
DOSFILE = '/Users/adammcmurchie/2021/fishwives/DOS/functions/' + choice


with open(DOSFILE) as f1:
	f1_text = f1.read()

with open(gameFile) as f2:
	f2_text = f2.read()

f1_text = f1_text.strip().splitlines()
f2_text = f2_text.strip().splitlines()

# Find and print the diff:
print("Printing the differences Game file has over Dos file: ")
for line in difflib.unified_diff(f1_text, f2_text, fromfile=DOSFILE, tofile=gameFile, lineterm=''):
	print(line)
	#if(line[0] == '+'): print(line)