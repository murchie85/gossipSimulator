"""

This function prints row of 3 boxed 


"""
import math
import time
from art import *
from .utils import med_print
import pygame
from ._game_functions import *
from .logging import *
import random





#************************************************************************************
#
#              ---------------NOTIFICATIONS--------------                          *
#
#************************************************************************************



blockLen     = 50
blocksPerRow = 3
updateFont = pygame.font.Font("resources/nokiafc.ttf", 16)

def stringMod(string,blockLen=50):
    allowedLen = blockLen - 4 # allow for | 
    difference = allowedLen - len(string)
    # pad with spaces
    if difference > 0:
        for i in range(0, difference):
            string += " "

    if difference < 0:
        string = string[:allowedLen]

    printString = "| " + string + " |"
    return(printString)



#  this will print a messages for a given time.
#  it counts down a timer to keep printing message
def printNotification(message, messageTime,SCREEN,WIDTH,HEIGHT,dialogueBox,imageDict):
    if message == "":
        return('free',messageTime)

    if messageTime >= 0:

        # THIS DRAWS THE BACKGROUND DIALOGUE BOX
        draw_backScaled(SCREEN,dialogueBox,0.2*WIDTH,0.7*HEIGHT,600,120)
        spacing = 0.04
        # THIS WRITES ROWS IN EQUAL LENGTH, PREVENTS LETTER CUTOFF
        rowLen,maxRL,words,i = 0,42,"",0
        if(len(message) <= maxRL):drawText(SCREEN,updateFont,str(message),0.026*WIDTH, 0.735*HEIGHT)
        for word in message.split():
            words+= word + ' '
            if(len(words) >= maxRL):
                drawText(SCREEN,updateFont,str(words),0.26*WIDTH, (0.735 + (i * spacing) )*HEIGHT)
                words = ""
                i+=1
        if(words!=""): drawText(SCREEN,updateFont,str(words),0.26*WIDTH,(0.735 + (i * spacing) )*HEIGHT)


        #draw_backScaled(SCREEN,imageDict['boyProfile'],0.8*WIDTH,0.6*HEIGHT,200,240)
        draw_backScaled(SCREEN,imageDict['girlProfile'],0.045*WIDTH,0.6*HEIGHT,180,220)

        messageTime -=1
        return('running',messageTime)

    if messageTime < 0:
        return('free',messageTime)



def logRandomUpdate(gossipUpdates,chosenGossip,filePath):
    if((len(gossipUpdates) > 0 )):
        oldGossip    = chosenGossip 
        if(oldGossip in gossipUpdates):
            return(chosenGossip)
        else:
            chosenGossip = random.choice(gossipUpdates)
            um = str('New Gossip: ' + str(chosenGossip['creator']) + " : " + str(chosenGossip['rumour'] + '\n'))
            logUpdateMessage(um,filePath)

    return(chosenGossip)







#************************************************************************************
#
#              ---------------DRAW--------------                          *
#
#************************************************************************************



def draw_sprite(SCREEN,sprite,sprite_pos,moving,facing,sprite_frame,snap,offset=vec(0,0),scaleVal=1):
    if(moving==0):
        sprite = sprite[facing][1]
    else:
        sprite = sprite[facing][sprite_frame]
    
    if(snap==1):
        # If sap, double size, pos = pos-offset * scaled val
        scaledSprite = pygame.transform.scale(sprite, (sprite.get_width()*scaleVal, sprite.get_height()*scaleVal))
        SCREEN.blit(scaledSprite, ((sprite_pos.x - offset.x) * scaleVal,(sprite_pos.y - offset.y)*scaleVal))
    else:
        SCREEN.blit(sprite, (sprite_pos.x,sprite_pos.y))



def draw_spriteScaled(SCREEN,Ark,ark_pos,moving,facing,sprite_frame,x,y):
    if(moving==0):
        Ark = Ark[facing][0]
    else:
        Ark = Ark[facing][sprite_frame]
    Ark = pygame.transform.scale(Ark, (x, y))

    SCREEN.blit(Ark, (ark_pos.x,ark_pos.y))

def draw_speechBubble(SCREEN,fonts,imageDict,x,y,message,snap,offset,scaleVal=2):
    
    # for text positioning
    bubbleL = 60
    bubbleH = 20
    # TODO, fix, if scaling changes, so does position of emoji

    if(snap==1):
        bubble = imageDict['speechBubble']
        scaledImage = pygame.transform.scale(bubble, (bubble.get_width()*scaleVal, bubble.get_height()*scaleVal))
        SCREEN.blit(scaledImage, (((x-(offset.x))*scaleVal) ,((y-offset.y)*scaleVal ) ))
        drawText(SCREEN,fonts['menuFont'], message,((x + 0.2 * bubbleL) - offset.x)  *scaleVal  ,((y + 0.3* bubbleH) - offset.y) * scaleVal,(0,0,0))
    else:
        bubble = imageDict['speechBubble']
        draw_back(SCREEN,imageDict['speechBubble'],x -10,y ,snap,vec(0,0))
        drawText(SCREEN,fonts['myfont'], message,x,y + 0.3* bubbleH,(0,0,0))




def draw_back(SCREEN,image,x,y,snap=0,offset=vec(0,0),fudge=2,zoomhScale=2,zoomvScale=2,nhScale=1,nvScale=1):
    # zoomscale overrides zoom scale
    # nscale overrides normal scale
    if(snap==1):
        scaledImage = pygame.transform.scale(image, (image.get_width()*zoomhScale, image.get_height()*zoomvScale))
        SCREEN.blit(scaledImage, (((x-(offset.x))*fudge) ,((y-offset.y)*fudge ) ))
    else:
        if(nhScale!=1 or nvScale!=1):
            image  = pygame.transform.scale(image, (image.get_width()*nhScale, image.get_height()*nvScale))
        SCREEN.blit(image, (x,y))



def draw_backScaled(SCREEN,image,x,y,sx,sy):
    image = pygame.transform.scale(image, (sx, sy))
    SCREEN.blit(image, (x,y))

def drawText(SCREEN,myfont, value,x,y,color=(255, 255, 255)):
    textsurface = myfont.render(value, False, color)
    SCREEN.blit(textsurface,(x,y))

def drawWindow(SCREEN):
    SCREEN.fill(BLACK)

    

def snapView(snap,keydown):
    if(keydown == "F"):
        snap+=1
        keydown = ""
    
    if(snap>1): snap=0

    return(snap,keydown)


#************************************************************************************
#
#              ---------------CAMERA--------------                          *
#
#************************************************************************************





def scroll(player,offset,offset_float,CONST):
    offset_float.x += (player.x - offset_float.x + CONST.x)
    offset_float.y += (player.y - offset_float.y + CONST.y)
    offset.x, offset.y = int(offset_float.x), int(offset_float.y)
    
    left_border  = 250
    right_border = 750

    top_border    = 150
    bottom_border = 590

    #offset.x = max(left_border, offset.x)
    #offset.x = min(offset.x, right_border - WIDTH)

    #offset.y = max(bottom_border, offset.y)
    #offset.y = min(offset.x, top_border - HEIGHT)
    
    return(offset,offset_float)
