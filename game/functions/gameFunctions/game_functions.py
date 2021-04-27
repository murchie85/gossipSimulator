import pygame 
from .sprite_sheet import *
from .config import *
import random

WHITE  = (255,255,255)
BLACK  = (0,0,0)
STC      = 32

def initialiseSprites(tileSize,spriteLocation,spriteCols=3):

	# -------------sprites-------------------
	ss          = spritesheet(spriteLocation)
	spriteArray = []

	# GET DOWN ROW
	for i in range(spriteCols):
		spriteArray.append(ss.image_at((i*STC, 0, STC, STC)))
	facingDown = spriteArray
	spriteArray = []

	# GET LEFT ROW
	for i in range(spriteCols):
		spriteArray.append(ss.image_at((i*STC, 2*STC, STC, STC)))
	facingLeft = spriteArray
	spriteArray = []

	# GET UP ROW
	for i in range(spriteCols):
		spriteArray.append(pygame.transform.flip(ss.image_at((i*STC, 4*STC, STC, STC)),True,False))
	
	facingUP = spriteArray
	spriteArray = []
	
	# GET RIGHT ROW
	for i in range(spriteCols):
		spriteArray.append(pygame.transform.flip(ss.image_at((i*STC, 2*STC, STC, STC)),True,False))
	facingRight = spriteArray
	spriteArray = []


	sprite = {"left": facingLeft, "right": facingRight, "up": facingUP, "down": facingDown}
	return(sprite)


def initialiseImageSpriteGroups(path,imageTotal,xscale,yscale):
	# if your images are numbered at the end like 1.jpg 2.jpg this will work
	## assumes images are 3 down 3 left, 3 up 
	imageArray = []

	# down
	for i in range(1,4):
		imagePath = path + str(i) + ".png"
		image   = pygame.image.load(imagePath)
		image   = pygame.transform.scale(image, (xscale, yscale))
		imageArray.append(image)
	facingDown = imageArray
	imageArray = []

	# left
	for i in range(4,7):
		imagePath = path + str(i) + ".png"
		image   = pygame.image.load(imagePath)
		image   = pygame.transform.scale(image, (xscale, yscale))
		imageArray.append(image)
	facingLeft = imageArray
	imageArray = []

	# up 
	for i in range(7,10):
		imagePath = path + str(i) + ".png"
		image   = pygame.image.load(imagePath)
		image   = pygame.transform.scale(image, (xscale, yscale))
		imageArray.append(image)
	facingUp = imageArray
	imageArray = []

	# right
	for i in range(4,7):
		imagePath = path + str(i) + ".png"
		image   = pygame.image.load(imagePath)
		image   = pygame.transform.scale(image, (xscale, yscale))
		image   = pygame.transform.flip(image,True,False)
		imageArray.append(image)
	facingRight = imageArray
	imageArray = []
	sprite = {"left": facingLeft, "right": facingRight, "up": facingUp, "down": facingDown}

	return(sprite)








def moveSprite(keys_pressed,pos,VEL,facing,moving):
	moving = 0
	if keys_pressed[pygame.K_LEFT] and pos.x - VEL > 0:
		pos.x -= VEL
		facing = 'left'
		moving = 1
	if keys_pressed[pygame.K_RIGHT] and pos.x + VEL + tileSize < WIDTH:
		pos.x += VEL
		facing = 'right'
		moving = 1
	if keys_pressed[pygame.K_UP] and pos.y - VEL > 0:
		pos.y -= VEL
		facing = 'up'
		moving = 1
	if keys_pressed[pygame.K_DOWN] and pos.y + VEL + tileSize < HEIGHT:
		pos.y += VEL
		facing = 'down'
		moving = 1

	return(pos, facing,moving)



def moveBotSprite(pos,botDirection,VEL,botfacing,citizen,citizen_list):
	moving = 0
	backoff = 0
	for key in citizen_list:
		otherCitizen = citizen_list[key]
		if otherCitizen != citizen:
			if pos.colliderect(otherCitizen['behaviour']['pos']):
				backoff = 1




	if (botDirection=='left') and pos.x - VEL > 0:
		pos.x -= VEL
		if(backoff): pos.x += 2 * VEL 
		botfacing = 'left'
	if (botDirection=='right') and pos.x + VEL + tileSize < WIDTH:
		pos.x += VEL
		if(backoff): pos.x -= 2 * VEL 
		botfacing = 'right'
	if (botDirection=='up') and pos.y - VEL > 0:
		pos.y -= VEL
		if(backoff): pos.y += 2 * VEL 
		botfacing = 'up'
	if (botDirection=='down') and pos.y + VEL + tileSize < HEIGHT:
		pos.y += VEL
		if(backoff): pos.y -= 2 * VEL 
		botfacing = 'down'

	return(pos,botDirection,botfacing)



def botWalkBehaviour(chosenDirection='none',chosenDuration=0):
	chosenDuration -= 1

	if(chosenDirection =='none' or chosenDuration < 0):
		chosenDirection = random.choice(['left','right','up','down','none'])
		chosenDuration = random.randint(1,10) * 10

	return(chosenDirection,chosenDuration) 






def events(run):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:run = False


	return(run)




def draw_sprite(SCREEN,Ark,ark_pos,moving,facing,sprite_frame):
	if(moving==0):
		Ark = Ark[facing][0]
	else:
		Ark = Ark[facing][sprite_frame]
		
	SCREEN.blit(Ark, (ark_pos.x,ark_pos.y))


def draw_spriteScaled(SCREEN,Ark,ark_pos,moving,facing,sprite_frame,x,y):
	if(moving==0):
		Ark = Ark[facing][0]
	else:
		Ark = Ark[facing][sprite_frame]
	Ark = pygame.transform.scale(Ark, (x, y))

	SCREEN.blit(Ark, (ark_pos.x,ark_pos.y))



def draw_back(SCREEN,image,x=0,y=0):
	SCREEN.blit(image, (x,y))


def drawText(SCREEN,myfont, value,x,y):
	textsurface = myfont.render(value, False, (255, 255, 255))
	SCREEN.blit(textsurface,(x,y))

def drawWindow(SCREEN):
	SCREEN.fill(BLACK)

	

def update():
	pygame.display.update()
