import pygame
from .sprite_sheet import *
from .config import *

WHITE  = (255,255,255)
BLACK  = (0,0,0)
STC      = 32

def initialiseSprites(tileSize):
	# -------------sprites-------------------
	ss          = spritesheet('/Users/adammcmurchie/2021/fishwives/sprites/characters/ArkJ.gif')
	ArkS        = ss.image_at((32, 0, STC, STC))
	facingDown  = ss.image_at((0, 0, STC, STC))
	facingUP    = ss.image_at((0, 4*32, STC, STC))
	facingLeft  = ss.image_at((0, 2*32, STC, STC))
	facingRight = pygame.transform.flip(facingLeft,True,False)

	Ark = {"left": facingLeft, "right": facingRight, "up": facingUP, "down": facingDown}

	return(Ark)


def moveSprite(keys_pressed,pos,VEL,facing):
	if keys_pressed[pygame.K_LEFT] and pos.x - VEL > 0:
		pos.x -= VEL
		facing = 'left'
	if keys_pressed[pygame.K_RIGHT] and pos.x + VEL + tileSize < WIDTH:
		pos.x += VEL
		facing = 'right'
	if keys_pressed[pygame.K_UP] and pos.y - VEL > 0:
		pos.y -= VEL
		facing = 'up'
	if keys_pressed[pygame.K_DOWN] and pos.y + VEL + tileSize < HEIGHT:
		pos.y += VEL
		facing = 'down'

	return(pos, facing)


def events(run):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:run = False


	return(run)




def draw_sprite(SCREEN,Ark,ark_pos):
	SCREEN.blit(Ark, (ark_pos.x,ark_pos.y))

def drawText(SCREEN,myfont, value):
	textsurface = myfont.render(value, False, (255, 255, 255))
	SCREEN.blit(textsurface,(0,0))

def drawWindow(SCREEN):
	SCREEN.fill(BLACK)

	

def update():
	pygame.display.update()
