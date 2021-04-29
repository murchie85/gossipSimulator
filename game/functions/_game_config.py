import pygame
from ._game_functions import *


WIDTH, HEIGHT = 1000 ,700
tileSize = 32

SCREEN  = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.font.init() 
myfont   = pygame.font.Font("resources/nokiafc.ttf", 8)
menuFont = pygame.font.Font("resources/nokiafc.ttf", 16)
VEL    = 2
BOTVEL = 1


#-------------------
# SPRITES 
#-------------------

Ark    = initialiseImageSpriteGroups('/Users/adammcmurchie/2021/fishwives/sprites/characters/ark/ark',12,32,32)



mainBackPath = "/Users/adammcmurchie/2021/fishwives/sprites/backgrounds/test.png"
mainBack     = pygame.image.load(mainBackPath).convert()
mainBack     = pygame.transform.scale(mainBack, (WIDTH, HEIGHT))



#---------------CREATING BOT SPRITES------------------------

spritePath  = '/Users/adammcmurchie/2021/fishwives/sprites/characters/'
spriteNames = ['ark','claude','Diane','Doug','Eberle','Ileyda','Jean','Philis','rick','Telmia','Vanrose','Yurald']
botSprites = []
for i in range(len(spriteNames)):
	path = spritePath + spriteNames[i] +'/' + spriteNames[i] 
	botSprite = initialiseImageSpriteGroups(path,9,32,32)
	botSprites.append(botSprite)

