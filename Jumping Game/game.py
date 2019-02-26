from pygame_functions import *
import random

screenSize(800,800)
setBackgroundColour("white")

points = 0

x = 200
y = 200

square = makeSprite("red.jpg")
transformSprite(square,0,0.1)
moveSprite(square,x,y)
showSprite(square)

drawLine(0,750,800,750,"black")

width = 600

alive = False

y_a = 1

y_v = 0

game = True

score = makeLabel(str(points),30,10,10)
showLabel(score)

while game:
	y_v += y_a
	if y > 700:
		y_v = 0
	if keyPressed("space") and y >= 111:
		y_v = -15
	if y + y_v > 700:
		y = 701
	else:
		y += y_v
	moveSprite(square,x,y)

	width -= 10
	if not alive:
		height = random.randint(0,700)
		width = 700
		star = makeSprite("star.png")
		transformSprite(star,0,0.05)
		moveSprite(star,width,height)
		showSprite(star)
		alive = True
	if width < 0:
		killSprite(star)
		alive = False
	moveSprite(star,width,height)

	if touching(square,star):
		killSprite(star)
		alive = False
		points += 1
		changeLabel(score,str(points))

	pause(10)


endWait()
