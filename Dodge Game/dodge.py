from pygame_functions import *
import random
import time

screenSize(800,750)
setBackgroundColour("white")


def end():
	hideSprite(character)
	hideSprite(wall)
	hideLabel(score)
	hideLabel(difficulty)
	finalScore = makeLabel("Your final score was: " + str(points),50,200,200)
	showLabel(finalScore)
	playAgain = makeSprite("playAgain.png")
	transformSprite(playAgain,0,0.8)
	moveSprite(playAgain,250,500)
	showSprite(playAgain)

	scoreList = []
	scoreSheet = open("scores.txt","r")
	for line in scoreSheet:
		if len(line)>1:
			newScore,newName = line[:-1].split(',')
			newScore = int(newScore)
			scoreList.append((newScore,newName))
	scoreSheet.close()
	scoreList.append((points, name))
	scoreList = sorted(scoreList)
	scoreSheet = open("scores.txt","w")
	for item in scoreList:
		scoreSheet.write(str(item[0]) + "," + item[1] + "\n")
	scoreSheet.close()
	high1 = scoreList[-1]
	high2 = scoreList[-2]
	high3 = scoreList[-3]
	highScore = makeLabel("Highest Scores:   " + str(high1[0]) + "   by  " + str(high1[1]) + "<br>                             " + str(high2[0]) + "   by  " + str(high2[1]) + "<br>                             " + str(high3[0]) + "   by  " + str(high3[1]) + "<br>",30,250,300)
	showLabel(highScore)
	endName = makeLabel("Well done " + name,50,250,30)
	showLabel(endName)

	again = True
	while again:
		pause(10)
		if spriteClicked(playAgain):
			hideLabel(finalScore)
			hideSprite(playAgain)
			hideLabel(highScore)
			hideLabel(endName)
			play()
def no():
	pass

def play():

	global character
	global wall
	global score
	global points
	global name
	global difficulty

	enterName = makeLabel("Enter your name:",60,200,100)
	showLabel(enterName)
	nameBox = makeTextBox(250,250,300,0,'Maximum 10 characters',10,32)
	criteria = makeLabel("(Only letters allowed)",30,225,400)
	showLabel(criteria)
	tryAgain = makeLabel("Please Try Again",30,325,350)
	name = ''
	valid = False
	count = 0
	while not valid:
		valid = True
		for x in name:
			if x not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
				valid = False
		if len(name) == 0:
			valid = False
		if not valid:
			if count > 0:
				showLabel(tryAgain)
			name,nothing = textBoxInput(nameBox,no,())
			count += 1
	hideLabel(enterName)
	hideTextBox(nameBox)
	hideLabel(criteria)
	hideLabel(tryAgain)


	x = 350
	y = 500

	character = makeSprite("star.png")
	transformSprite(character,0,0.1)
	moveSprite(character,x,y)
	showSprite(character)

	wallx = random.randint(-650,-50)
	wally = -400

	wall = makeSprite("red.png")
	transformSprite(wall,0,3)
	moveSprite(wall,wallx,wally)
	showSprite(wall)

	points = 0
	score = makeLabel("Score: " + str(points),30,10,10)
	showLabel(score)

	level = 10
	difficulty = makeLabel("Level: " + str(level),30,650,10)
	showLabel(difficulty)

	game = True
	extra = 0
	start = time.time()
	while game:
		now = time.time()
		extra = (now-start) // 5
		level = 10 + extra
		levels = round(level,0)
		changeLabel(difficulty,"Level: " + str(levels))
		if keyPressed("right") and x < 650:
			x += level
		if keyPressed("left") and x > 25:
			x-= level
		moveSprite(character,x,y)
		wally += level
		moveSprite(wall,wallx,wally)
		if wally > 700:
			wallx = random.randint(-650,-50)
			wally = -300
			moveSprite(wall,wallx,wally)
			showSprite(character)
			points += 1
			changeLabel(score,"Score: " + str(points))

		if touching(character,wall):
			game = False
	end()

play()


endWait()