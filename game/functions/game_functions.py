import pygame
from .sprite_sheet import *


WHITE  = (255,255,255)
BLACK  = (0,0,0)
STC      = 32

def initialiseSprites(tileSize):
	# -------------sprites-------------------
	ss = spritesheet('/Users/adammcmurchie/2021/fishwives/sprites/characters/ArkJ.gif')
	ArkS = ss.image_at((32, 0, STC, STC))
	ArkD = ss.image_at((0, 0, STC, STC))
	ArkU = ss.image_at((0, 4*32, STC, STC))
	ArkL = ss.image_at((0, 2*32, STC, STC))
	Ark = pygame.transform.scale(ArkL,(tileSize,tileSize))

	return(Ark)


def moveSprite(keys_pressed,ark_pos,VEL):
	if keys_pressed[pygame.K_a]:
		ark_pos.x -= VEL
	if keys_pressed[pygame.K_d]:
		ark_pos.x += VEL
	if keys_pressed[pygame.K_w]:
		ark_pos.y -= VEL
	if keys_pressed[pygame.K_s]:
		ark_pos.y += VEL

	return(ark_pos)


def events(run):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:run = False


	return(run)


def draw(WIN,Ark,ark_pos):
	WIN.fill(BLACK)
	WIN.blit(Ark, (ark_pos.x,ark_pos.y))

	

def update():
	pygame.display.update()
