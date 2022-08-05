import pygame
from ._game_functions import *
import os

WIDTH, HEIGHT = 1000 ,700
tileSize = 32
#, pygame.NOFRAME
SCREEN  = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.font.init() 
myfont   = pygame.font.Font("resources/nokiafc.ttf", 8)
menuFont = pygame.font.Font("resources/nokiafc.ttf", 16)
baseDir  = os.path.dirname(os.getcwd())


## CAMERA
vec = pygame.math.Vector2
offset = vec(0,0)
offset_float = vec(0,0)

# The plus values change center, but map pos is off.
CONST = vec(-WIDTH / 2 + 300, -HEIGHT / 2 + 200)
snap =0
sprite_frame=0
keydown = False
moving = 0
ark_pos     = pygame.Rect(WIDTH/2,HEIGHT/2,tileSize/2,tileSize/2)

clock       = pygame.time.Clock()
run         = True                 # When False game exits
gameCounter = 0                    # loop count 
frameSwitch = 0                    # var to let us know the frame has been switched and to wait
FPS         = 20                   # PS
facing      = 'down'
nextFrame   = pygame.time.get_ticks()

noticationStatus = ""












fonts = {'myfont':myfont,'menuFont':menuFont}

VEL    = 8
BOTVEL = 1


#-------------------
# SPRITES 
#-------------------

Ark    = initialiseImageSpriteGroups(baseDir + '/sprites/characters/ark/ark',12,32,32)



mainBackPath = baseDir + "/sprites/backgrounds/test.png"
mainBack     = pygame.image.load(mainBackPath).convert()
mainBack     = pygame.transform.scale(mainBack, (WIDTH, HEIGHT))

DialoguePath = baseDir + "/sprites/dialoguebox/dbox.png"
Dialoguebox  = pygame.image.load(DialoguePath).convert()

arrowLeft      = baseDir + "/sprites/arrow/arrow1.png"
arrowLeft      = pygame.image.load(arrowLeft)
arrowRight     = baseDir + "/sprites/arrow/arrow2.png"
arrowRight     = pygame.image.load(arrowRight)


menuOptionOne   = baseDir + "/sprites/menu/menuOptions1.png"
menuOptionTwo   = baseDir + "/sprites/menu/menuOptions2.png"
menuOptionThree = baseDir + "/sprites/menu/menuOptions3.png"
menuOptionFour  = baseDir + "/sprites/menu/menuOptions4.png"
menuOptionFive  = baseDir + "/sprites/menu/menuOptions5.png"
mOptionOne   = pygame.image.load(menuOptionOne)
mOptionTwo   = pygame.image.load(menuOptionTwo)
mOptionThree = pygame.image.load(menuOptionThree)
mOptionFour  = pygame.image.load(menuOptionFour)
mOptionFive  = pygame.image.load(menuOptionFive)
mOptionArray = [mOptionOne,mOptionTwo,mOptionThree,mOptionFour,mOptionFive]


emoji1  = baseDir + "/sprites/emoji/emojis1.png"
emoji2  = baseDir + "/sprites/emoji/emojis2.png"
emoji3  = baseDir + "/sprites/emoji/emojis3.png"
emoji4  = baseDir + "/sprites/emoji/emojis4.png"
emoji5  = baseDir + "/sprites/emoji/emojis5.png"
emoji1   = pygame.image.load(emoji1)
emoji2   = pygame.image.load(emoji2)
emoji3   = pygame.image.load(emoji3)
emoji4   = pygame.image.load(emoji4)
emoji5   = pygame.image.load(emoji5)
emojis = [emoji1,emoji2,emoji3,emoji4,emoji5]


speechBubble = baseDir + "/sprites/speech/bubble.png"
speechBubble  = pygame.image.load(speechBubble)

girlProfile  = baseDir + "/sprites/characterProfile/small/Erika.png"
girlProfile  = pygame.image.load(girlProfile)
lGirl,wGirl  = 346, 461
girlProfile  = pygame.transform.scale(girlProfile, (lGirl,wGirl ))

boyProfile  = baseDir + "/sprites/characterProfile/boy.png"
boyProfile  = pygame.image.load(boyProfile)
boyProfile  = pygame.transform.scale(boyProfile, (200, 240))

imageDict = {"mainBack":mainBack, 
			 "Dialoguebox":Dialoguebox, 
			 "arrowLeft":arrowLeft,
			 "arrowRight":arrowRight,
			 "mOptionArray":mOptionArray,
			 "emojis": emojis,
			 "speechBubble": speechBubble,
			 "girlProfile":{'sprite': girlProfile, 'l':lGirl,'w':wGirl},
			 "boyProfile":boyProfile}  
  

#---------------CREATING BOT SPRITES------------------------

spritePath  = baseDir + '/sprites/characters/'
males   = ['claude,male''Doug,male','Jean,male','rick,male','Vanrose,male','Yurald,male']
females = ['Diane,female', 'Eberle,female','Ileyda,female', 'Philis,female', 'Telmia,female']



# POPULATES botSprites with two lists of male,female and their sprite associations
botSprites  = []
maleSprites = []
for i in range(len(males)):
	path = spritePath + males[i].split(',')[0] +'/' + males[i].split(',')[0] 
	botSprite = initialiseImageSpriteGroups(path,9,32,32)
	maleSprites.append(botSprite)

femaleSprites = []
for i in range(len(females)):
	path = spritePath + females[i].split(',')[0] +'/' + females[i].split(',')[0] 
	botSprite = initialiseImageSpriteGroups(path,9,32,32)
	femaleSprites.append(botSprite)

botSprites.append(maleSprites)
botSprites.append(femaleSprites)

