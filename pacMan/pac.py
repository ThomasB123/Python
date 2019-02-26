from pygame_functions import *

screenSize(700,700)
setBackgroundColour("white")



pacMan = makeSprite("pacman.png")
transformSprite(pacMan,0,0.05)
moveSprite(pacMan,100,100)
showSprite(pacMan)


def man():
	global x
	global y
	speed = 5
	if keyPressed("right") and x < 650:
		x += speed
	if keyPressed("left") and x > 0:
		x -= speed
	if keyPressed("up") and y > 0:
		y -= speed
	if keyPressed("down") and y < 650:
		y += speed

	moveSprite(pacMan,x,y)



ghost = makeSprite("blue.png")
transformSprite(ghost,0,0.06)
moveSprite(ghost,300,300)
showSprite(ghost)


def moveGhost():
	global ghostx
	global ghosty
	speed = 2
	if ghostx > x:
		ghostx -= speed
	if ghostx < x:
		ghostx += speed
	if ghosty > y:
		ghosty -= speed
	if ghosty < y:
		ghosty += speed

	moveSprite(ghost,ghostx,ghosty)



game = True

global x
global y
x = 100
y = 100

global ghostx
global ghosty
ghostx = 300
ghosty = 300

while game:
	man()
	moveGhost()
	pause(10)























endWait()