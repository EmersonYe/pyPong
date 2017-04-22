import pygame, sys
from pygame.locals import *

FPS = 200
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

def main():
	pygame.init()
	global DISPLAYSURF
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
	pygame.display.set_caption("Pong")

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

				