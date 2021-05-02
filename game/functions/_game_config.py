import pygame
from ._game_functions import *


WIDTH, HEIGHT = 1000 ,700
tileSize = 32
SCREEN  = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.font.init() 
myfont   = pygame.font.Font("resources/nokiafc.ttf", 8)
menuFont = pygame.font.Font("resources/nokiafc.ttf", 16)



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
FPS         = 40                   # PS
facing      = 'down'
nextFrame   = pygame.time.get_ticks()

noticationStatus = ""












fonts = {'myfont':myfont,'menuFont':menuFont}

VEL    = 5
BOTVEL = 1


#-------------------
# SPRITES 
#-------------------

Ark    = initialiseImageSpriteGroups('/Users/adammcmurchie/2021/fishwives/sprites/characters/ark/ark',12,32,32)



mainBackPath = "/Users/adammcmurchie/2021/fishwives/sprites/backgrounds/test.png"
mainBack     = pygame.image.load(mainBackPath).convert()
mainBack     = pygame.transform.scale(mainBack, (WIDTH, HEIGHT))

DialoguePath = "/Users/adammcmurchie/2021/fishwives/sprites/dialoguebox/dbox.png"
Dialoguebox  = pygame.image.load(DialoguePath).convert()




#---------------CREATING BOT SPRITES------------------------

spritePath  = '/Users/adammcmurchie/2021/fishwives/sprites/characters/'
spriteNames = ['claude','Diane','Doug','Eberle','Ileyda','Jean','Philis','rick','Telmia','Vanrose','Yurald']
botSprites = []
for i in range(len(spriteNames)):
	path = spritePath + spriteNames[i] +'/' + spriteNames[i] 
	botSprite = initialiseImageSpriteGroups(path,9,32,32)
	botSprites.append(botSprite)

