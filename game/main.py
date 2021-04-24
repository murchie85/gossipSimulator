import pygame
import os
from sprite_sheet import *
from config import *


WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Celestus")

WHITE  = (255,255,255)
BLACK  = (0,0,0)

STC      = 32
tileSize = 64

FPS = 60 


# -------------sprites-------------------

ss = spritesheet('../sprites/characters/ArkJ.gif')
ArkS = ss.image_at((32, 0, STC, STC))
ArkD = ss.image_at((0, 0, STC, STC))
ArkU = ss.image_at((0, 4*32, STC, STC))
ArkL = ss.image_at((0, 2*32, STC, STC))
Ark = pygame.transform.scale(ArkL,(tileSize,tileSize))



ss = spritesheet('../sprites/characters/Diane.gif')
Diane = ss.image_at((0, 0, tileSize, tileSize))
DianeS = ss.image_at((32, 0, STC, STC))
DianeD = ss.image_at((0, 0, STC, STC))
DianeU = ss.image_at((0, 4*32, STC, STC))
DianeL = ss.image_at((0, 2*32, STC, STC))
Diane = pygame.transform.scale(DianeL,(tileSize,tileSize))
#PLAYER_CHARACTER_IMAGE = pygame.image.load('../sprites/characters/') 
# ----------------------------------------



def events(run):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:run = False


	return(run)


def draw(WIN,ark_pos,diane_pos):
	WIN.fill(BLACK)
	WIN.blit(Ark, (ark_pos.x,ark_pos.y))
	WIN.blit(Diane, (diane_pos.x,diane_pos.y))
	#font = pygame.font.Font('Arial', 32)
	

def update():
	pygame.display.update()


def main():
	ark_pos = pygame.Rect(100,300,tileSize,tileSize)
	diane_pos = pygame.Rect(700,300,tileSize,tileSize)

	clock = pygame.time.Clock()
	run = True


	while run:
		clock.tick(FPS)
		run = events(run)

		draw(WIN, ark_pos,diane_pos)
		update()





	pygame.quit()
	print('Exiting...')



if __name__ == '__main__':
	main()