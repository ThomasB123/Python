from pygame_functions import *
import time
import random

class TrieNode:
    def __init__(self, parent, value):
        self.parent = parent
        self.children = [None] * 26
        self.isWord = False
        self.value = value
        if parent is not None:
            parent.children[ord(value)-97] = self

def makeTrie(dictionary):
    dict = open(dictionary)
    root = TrieNode(None,'')
    for word in dict:
        curNode = root
        for letter in word.lower():
            if 97 <= ord(letter) < 123:
                nextNode = curNode.children[ord(letter)-97]
                if nextNode is None:
                    nextNode = TrieNode(curNode,letter)
                curNode = nextNode
        curNode.isWord = True
    return root

def searchTrie(word):
    isThere = False
    curNode = root
    for letter in word.lower():
        if 97 <= ord(letter) < 123:
            curNode = curNode.children[ord(letter)-97]
            if curNode is None:
                return isThere
    if curNode.isWord == True:
        isThere = True
    return isThere

def letterFrequency(dictionary):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = []
    for x in range(len(alphabet)):
        for y in range(dictionary[alphabet[x]]):
            letters.append(alphabet[x])
    return letters

def createGrid():
    grid = []
    for row in range(4):
        grid.append([])
        for column in range(4):
            grid[row].append(" ")
    return grid

def fillGrid(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            grid[x][y] = letters[random.randint(0,999)]
    return grid

def validNeighbours(x,y):
    neighbours = []
    if x < 3:
        neighbours.append([x+1,y])
        if y < 3:
            neighbours.append([x+1,y+1])
        if y > 0:
            neighbours.append([x+1,y-1])        
    if x > 0:
        neighbours.append([x-1,y])
        if y < 3:
            neighbours.append([x-1,y+1])
        if y > 0:
            neighbours.append([x-1,y-1])        
    if y < 3:
        neighbours.append([x,y+1])
    if y > 0:
        neighbours.append([x,y-1])
    return(neighbours)

def translate(list):
    word = ''
    for x in range(len(list)):
        word += fullGrid[list[x][0]][list[x][1]]
    return word

def searchStub(stub):
    isThere = True
    curNode = root
    for letter in stub.lower():
        if 97 <= ord(letter) < 123:
            nextNode = curNode.children[ord(letter)-97]
            if nextNode is not None:
                curNode = nextNode
            else:
                return False
    return isThere

def possibleWords(fullGrid):
    possible = []
    queue = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            queue.append([[x,y]])
    while len(queue) > 0:
        current = queue[0]
        stub = translate(current)
        if searchStub(stub):
            neighbours = validNeighbours(current[-1][0], current[-1][1])
            for a in range(len(neighbours)):
                add = []
                if neighbours[a] not in current:
                    for b in range(len(current)):
                        add.append(current[b])
                    add.append(neighbours[a])
                    if searchStub(translate(add)):
                        queue.append(add)
            if searchTrie(stub) and stub not in possible:
                possible.append(stub)
        del queue[0]
    return possible

def longestWords(words):
    if len(words[-1]) != len(words[-2]):
        out = "The longest possible word was:<br>"
    else:
        out = "The longest possible words were:<br>"
    counter = -1
    while len(words[counter]) == len(words[-1]):
        out += "<br>" + str(words[counter])
        counter -= 1
    return out + "<br>"

def longestCorrect(correct):
    length = len(correct)
    if length == 0:
        return "You didn't play any correct words."
    out = "The longest word you played was:<br>"
    if length == 1:
        return out + "<br>" + str(correct[0]) + "<br>"
    correct = sorted(correct,key=len)
    if len(correct[-1]) != len(correct[-2]):
        return out + "<br>" + str(correct[-1]) + "<br>"
    out = "The longest words you played were:<br>"
    out += "<br>" + str(correct[length-1])
    counter = 2
    while len(correct[-1]) == len(correct[length-counter]) and counter < length+1:
        out += "<br>" + str(correct[length-counter])
        counter += 1
    return out + "<br>"

englishFrequency = {'A':84,'B':16,'C':29,'D':44,'E':132,'F':23,'G':21,'H':62,'I':71,'J':3,'K':9,'L':5,'M':25,'N':68,'O':77,'P':20,'Q':2,'R':61,'S':64,'T':93,'U':29,'V':11,'W':25,'X':3,'Y':21,'Z':2}
frenchFrequency = {'A':81,'B':9,'C':34,'D':37,'E':167,'F':11,'G':9,'H':7,'I':76,'J':6,'K':1,'L':55,'M':30,'N':71,'O':58,'P':25,'Q':14,'R':67,'S':79,'T':72,'U':64,'V':18,'W':1,'X':4,'Y':1,'Z':3}
germanFrequency = {'A':71,'B':19,'C':27,'D':51,'E':163,'F':17,'G':30,'H':46,'I':66,'J':3,'K':14,'L':34,'M':25,'N':98,'O':30,'P':7,'Q':1,'R':70,'S':74,'T':62,'U':52,'V':8,'W':19,'X':1,'Y':1,'Z':11}
spanishFrequency = {'A':111,'B':22,'C':40,'D':50,'E':159,'F':7,'G':18,'H':7,'I':61,'J':5,'K':1,'L':50,'M':32,'N':66,'O':86,'P':25,'Q':9,'R':68,'S':79,'T':46,'U':29,'V':11,'W':1,'X':2,'Y':10,'Z':5}


def startGame():
    global background
    global output
    global points
    global score
    global timer
    global remaining
    global wordsLeft
    global textBox
    global correct
    global label1
    global label2
    global label3
    global label4
    global label5
    global label6
    global label7
    global label8
    global label9
    global label10
    global label11
    global label12
    global label13
    global label14
    global label15
    global label16
    background = makeSprite("Grid.png")
    moveSprite(background,80,80)
    transformSprite(background,0,1.2)
    showSprite(background)
    output = makeLabel("Welcome",25,500,100)
    showLabel(output)
    points = 0
    score = makeLabel("Score: " + str(points),30,500,200)
    showLabel(score)
    timer = makeLabel("Time: " + str(t),30,500,300)
    showLabel(timer)
    remaining = len(words)
    wordsLeft = makeLabel("There are " + str(remaining) + " words left",25,500,400)
    showLabel(wordsLeft)
    textBox = makeTextBox(100,500,400,0,'',16,32)
    correct = []
    label1 = makeLabel(fullGrid[0][0],24,100,100)
    label2 = makeLabel(fullGrid[0][1],24,100,200)
    label3 = makeLabel(fullGrid[0][2],24,100,300)
    label4 = makeLabel(fullGrid[0][3],24,100,400)
    label5 = makeLabel(fullGrid[1][0],24,200,100)
    label6 = makeLabel(fullGrid[1][1],24,200,200)
    label7 = makeLabel(fullGrid[1][2],24,200,300)
    label8 = makeLabel(fullGrid[1][3],24,200,400)
    label9 = makeLabel(fullGrid[2][0],24,300,100)
    label10 = makeLabel(fullGrid[2][1],24,300,200)
    label11 = makeLabel(fullGrid[2][2],24,300,300)
    label12 = makeLabel(fullGrid[2][3],24,300,400)
    label13 = makeLabel(fullGrid[3][0],24,400,100)
    label14 = makeLabel(fullGrid[3][1],24,400,200)
    label15 = makeLabel(fullGrid[3][2],24,400,300)
    label16 = makeLabel(fullGrid[3][3],24,400,400)
    showLabel(label1)
    showLabel(label2)
    showLabel(label3)
    showLabel(label4)
    showLabel(label5)
    showLabel(label6)
    showLabel(label7)
    showLabel(label8)
    showLabel(label9)
    showLabel(label10)
    showLabel(label11)
    showLabel(label12)
    showLabel(label13)
    showLabel(label14)
    showLabel(label15)
    showLabel(label16)
    global chosenLang
    chosenLang = makeLabel("You are playing in " + language,25,100,20)
    showLabel(chosenLang)
    global start
    start = clock()

def loading():
    global load
    hideLabel(welcome)
    hideLabel(menuText)
    hideSprite(french)
    hideSprite(english)
    load = makeLabel("Loading...",60,250,250)
    showLabel(load)

def no():
    pass

def menu():
    global name
    global welcome
    global menuText
    global french 
    global english
    global root
    global letters
    global grid
    global fullGrid
    global words
    boggle = makeLabel("Welcome to Boggle",70,150,25)
    showLabel(boggle)
    rules = makeLabel('''You will be shown a 4x4 grid of letters.<br>You must make as many words as you can within the time limit.<br>The longer the word, the more points it scores.<br>''',35,25,180)
    showLabel(rules)
    rules2 = makeLabel('''Words can only be made according to the following rules:<br>1. The letters must be adjoined in a ‘chain’ (vertically, horizontally or diagonally).<br>2. Words must contain at least three letters.<br>3. No letter cube may be used more than once within a single word<br>''',25,25,300)
    showLabel(rules2)
    pointsInfo = makeLabel("Letters:           Points:<br>3 or 4 letters   1 point<br>5 letters          2 points<br>6 letters          3 points<br>7 letters          5 points<br>8+ letters        11 points<br><br>",30,20,450)
    showLabel(pointsInfo)
    play = makeSprite("play.png")
    transformSprite(play,0,0.2)
    moveSprite(play,300,450)
    showSprite(play)
    playing = False
    while not playing:
        if spriteClicked(play):
            playing = True
        pause(10)
    hideLabel(boggle)
    hideLabel(rules)
    hideLabel(rules2)
    hideLabel(pointsInfo)
    hideSprite(play)
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
    welcome = makeLabel("Welcome " + str(name),60,200,50)
    showLabel(welcome)
    menuText = makeLabel("Select a language: ",60,170,200)
    showLabel(menuText)
    french = makeSprite("FrenchButton.png")
    transformSprite(french,0,0.6)
    moveSprite(french,400,400)
    showSprite(french)
    english = makeSprite("EnglishButton.png")
    transformSprite(english,0,0.33)    
    moveSprite(english,200,400)
    showSprite(english)
    menu = True
    global language
    while menu:
        if spriteClicked(french) == True:
            loading()
            start = time.time()
            root = makeTrie("french.txt")
            #334,871 words
            end = time.time()
            #print(end-start)
            letters = letterFrequency(frenchFrequency)
            menu = False
            language = "French"
        if spriteClicked(english) == True:
            loading()
            start = time.time()
            root = makeTrie("english.txt")
            #64,920 words
            end = time.time()
            #print(end-start)
            letters = letterFrequency(englishFrequency)
            menu = False
            language = "English"
        pause(10)
    grid = createGrid()
    fullGrid = fillGrid(grid)
    words = possibleWords(fullGrid)
    while len(words) < 20:
        fullGrid = fillGrid(grid)
        words = possibleWords(fullGrid)
    #print(words)
    #print(len(words))
    hideLabel(load)
    startGame()

def endGame(attempt):
    hideLabel(label1)
    hideLabel(label2)
    hideLabel(label3)
    hideLabel(label4)
    hideLabel(label5)
    hideLabel(label6)
    hideLabel(label7)
    hideLabel(label8)
    hideLabel(label9)
    hideLabel(label10)
    hideLabel(label11)
    hideLabel(label12)
    hideLabel(label13)
    hideLabel(label14)
    hideLabel(label15)
    hideLabel(label16)
    hideSprite(background)
    hideLabel(output)
    hideLabel(score)
    hideTextBox(textBox)
    hideLabel(timer)
    hideLabel(wordsLeft)
    hideLabel(chosenLang)
    couldHave = longestWords(words)
    didPlay = longestCorrect(correct)
    possible = makeLabel(couldHave, 23, 25, 420, "black", "Arial", "white")
    played = makeLabel(didPlay, 23, 425, 420, "black", "Arial", "white")
    showLabel(possible)    
    showLabel(played)
    if len(words) == len(correct):
        info = makeLabel("Well done! You found all of the words!",30,100,100)
    elif attempt == "EXITGAME":
        info = makeLabel("You chose to exit the game",30,220,100)
    else:
        info = makeLabel("You are out of time",30,250,100)
    showLabel(info)
    yourScore = makeLabel("Your final score was:",30,50,300)
    showLabel(yourScore)
    finalScore = makeLabel(str(points),100,120,335)
    showLabel(finalScore)
    scoreList = []
    #scoreSheet = open(language.lower()+"Scores.txt","r")
    if language == "French":
        scoreSheet = open("frenchScores.txt","r")
    if language == "English":
        scoreSheet = open("englishScores.txt","r")
    for line in scoreSheet:
        if len(line)>1:
            newScore,newName = line[:-1].split(',')
            newScore = int(newScore)
            scoreList.append((newScore,newName))
    scoreSheet.close()
    scoreList.append((points, name))
    scoreList = sorted(scoreList)
    #scoreSheet = open(language.lower()+"Scores.txt","w")
    if language == "French":
        scoreSheet = open("frenchScores.txt","w")
    if language == "English":
        scoreSheet = open("englishScores.txt","w")
    for item in scoreList:
        scoreSheet.write(str(item[0]) + "," + item[1] + "\n")
    scoreSheet.close()
    high1 = scoreList[-1]
    high2 = scoreList[-2]
    high3 = scoreList[-3]
    highScore = makeLabel("Highest Scores:   " + str(high1[0]) + "   by  " + str(high1[1]) + "<br>    (In "+ language + ")      " + str(high2[0]) + "   by  " + str(high2[1]) + "<br>                             " + str(high3[0]) + "   by  " + str(high3[1]) + "<br>",30,370,300)
    showLabel(highScore)
    endName = makeLabel("Well done " + name,50,250,30)
    showLabel(endName)
    playAgain = makeSprite("playAgain.png")
    moveSprite(playAgain,200,130)
    transformSprite(playAgain,0,0.5)
    showSprite(playAgain)
    replay = True
    while replay:
        if spriteClicked(playAgain):
            hideLabel(possible)
            hideLabel(played)
            hideLabel(info)
            hideLabel(yourScore)
            hideLabel(finalScore)
            hideLabel(highScore)
            hideLabel(endName)
            hideSprite(playAgain)
            global running
            running = True
            replay = False
            menu()
        pause(10)

t = 180
screenSize(800,700)
setBackgroundColour("white")
menu()

start = clock()
def countdown(t,start):
    now = clock()
    diff = (now-start)//1000
    left = t - diff
    left = round(left,0)
    if left < 0:
        return False
    else:
        changeLabel(timer,"Time: "+ str(left))
        return True

running = True
while running:
    attempt, running = textBoxInput(textBox,countdown,(t,start))
    attempt = attempt.upper()
    if attempt == "EXITGAME":
        running = False
    length = len(attempt)
    if length < 3:
        changeLabel(output, " Words must be 3 letters or more ", background = "red")
    elif attempt in words:
        if attempt in correct:
            changeLabel(output, " You have already played this word ", background = "red")
        else:
            if length == 3 or length == 4:
                points += 1
            if length == 5:
                points += 2
            if length == 6:
                points += 3
            if length == 7:
                points += 5
            if length >= 8:
                points += 11
            changeLabel(score,"Score: " + str(points))
            remaining -= 1
            changeLabel(wordsLeft,"There are " + str(remaining) + " words left")
            changeLabel(output, " Correct ", background = "green")
            correct.append(attempt)
            if len(correct) == len(words):
                changeLabel(output, " Well done! You found all of the words ", background = "green")
                running = False
    else:
        changeLabel(output," Not a valid word ", background="red")
    end = time.time()
    if not running:
        endGame(attempt)

endWait()
