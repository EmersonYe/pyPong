import pygame, sys
from pygame.locals import *

FPS = 200
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 20

BLACK = (0,0,0)
WHITE = (255,255,255)

def main():
	pygame.init()
	global DISPLAYSURF
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
	pygame.display.set_caption("Pong")

	ballX = WINDOWWIDTH/2 - LINETHICKNESS/2
	ballY = WINDOWHEIGHT/2 - LINETHICKNESS/2

	playerOnePosition = (WINDOWHEIGHT - PADDLESIZE)/2
	playerTwoPosition = (WINDOWHEIGHT - PADDLESIZE)/2

	paddle1 = pygame.Rect(PADDLEOFFSET,playerOnePosition,LINETHICKNESS,PADDLESIZE)
	paddle2 = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS,playerTwoPosition,LINETHICKNESS,PADDLESIZE)
	ball = pygame.Rect(ballX,ballY,LINETHICKNESS,LINETHICKNESS)

	def drawArena():
		DISPLAYSURF.fill(BLACK)
		pygame.draw.rect(DISPLAYSURF,WHITE,((0,0),(WINDOWWIDTH,WINDOWHEIGHT)),LINETHICKNESS*2)
		pygame.draw.line(DISPLAYSURF,WHITE, (WINDOWWIDTH/2,0),(WINDOWWIDTH/2,WINDOWHEIGHT),int(LINETHICKNESS/4))

	def drawPaddle(paddle):
		pygame.draw.rect(DISPLAYSURF,WHITE,paddle)

	def drawBall(ball):
		pygame.draw.rect(DISPLAYSURF,WHITE,ball)

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()
		FPSCLOCK.tick(FPS)

		drawArena()
		drawPaddle(paddle1)
		drawPaddle(paddle2)
		drawBall(ball)

if __name__ == '__main__':
	main()