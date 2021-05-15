import pygame 
from ._game_config import *
import random

WHITE  = (255,255,255)
BLACK  = (0,0,0)
STC      = 32
tileSize = 32
vec = pygame.math.Vector2

#************************************************************************************
#
#              ---------------SPRITES--------------                          *
#
#************************************************************************************



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








def moveSprite(keys_pressed,pos,VEL,facing,moving,WIDTH,HEIGHT,citizen_list,backgroundObjectMasks):
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

    #Check if colliding with any object
    collisionObjects   = []
    collisionTolerance = 10

    for key in citizen_list: collisionObjects.append(citizen_list[key]['movement']['pos'])
    for obj in backgroundObjectMasks: collisionObjects.append(obj)
    for otherObj in collisionObjects:
        
        if pos.colliderect(otherObj):
            if abs(otherObj.top - pos.bottom) < collisionTolerance:
                pos.y -= VEL
            if abs(otherObj.bottom - pos.top) < collisionTolerance:
                pos.y += VEL
            if abs(otherObj.right - pos.left) < collisionTolerance:
                pos.x += VEL
            if abs(otherObj.left - pos.right) < collisionTolerance:
                pos.x -= VEL



    return(pos, facing,moving)


#************************************************************************************
#
#              ---------------COLLISIONS AND BEHAVIOUR--------------                          *
#
#************************************************************************************




def moveBotSprite(pos,botDirection,BOTVEL,botfacing,citizen,citizen_list,WIDTH,HEIGHT,backgroundObjectMasks):
    moving = 0


    if (botDirection=='left') and pos.x - BOTVEL > 0:
        pos.x -= BOTVEL
        botfacing ='left'
        moving = 1
    if (botDirection=='right') and pos.x + BOTVEL + tileSize < WIDTH:
        pos.x += BOTVEL
        botfacing ='right'
        moving = 1
    
    if (botDirection=='up') and pos.y - BOTVEL > 0:
        pos.y -= BOTVEL
        botfacing='up'
        moving = 1
    if (botDirection=='down') and pos.y + BOTVEL + tileSize < HEIGHT:
        pos.y += BOTVEL
        botfacing='down'
        moving = 1



    #Check if colliding with any object
    collisionObjects   = []
    collisionTolerance = 10

    for key in citizen_list: 
        if(citizen_list[key]['name'] == citizen['name']):
            continue
        collisionObjects.append(citizen_list[key]['movement']['pos'])

    for obj in backgroundObjectMasks: collisionObjects.append(obj)
    
    for otherObj in collisionObjects:
        if pos.colliderect(otherObj):
            if abs(otherObj.top - pos.bottom) < collisionTolerance:
                pos.y -= 2*BOTVEL
                botDirection = random.choice(['left','right','down','up','none'])
            if abs(otherObj.bottom - pos.top) < collisionTolerance:
                pos.y += 2*BOTVEL
                botDirection = random.choice(['left','right','down','up','none'])
            if abs(otherObj.right - pos.left) < collisionTolerance:
                pos.x += BOTVEL
                botDirection = random.choice(['left','right','down','up','none'])
            if abs(otherObj.left - pos.right) < collisionTolerance:
                pos.x -= 2*BOTVEL
                botDirection = random.choice(['left','right','down','up','none'])



    return(pos,botDirection,botfacing)




def botWalkBehaviour(chosenDirection='none',chosenDuration=0):
    chosenDuration -= 1

    if(chosenDuration < 0):
        chosenDirection = random.choice(['right','down','left','up','none','none'])
        chosenDuration = random.randint(1,8) * 10

    return(chosenDirection,chosenDuration) 



def createCollisionMask(maskObject, x,y,objLen,objHeight):
    maskObject = pygame.Rect(x,y,objLen,objHeight)


#************************************************************************************
#
#              ---------------EVENTS--------------                          *
#
#************************************************************************************



def events(run,keydown):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:run = False
        
        if (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_f:
                keydown = "F"


    return(run,keydown)



def update():
    pygame.display.update()



