import time
import random

class TrieNode:
    def __init__(self, parent, value):
        self.parent = parent
        self.children = [None] * 26
        self.hasChildren = False
        self.isWord = False
        self.value = value
        if parent is not None:
            parent.children[ord(value)-97] = self

def makeTrie(dictionary):
    dict = open(dictionary)
    root = TrieNode(None, '')
    for word in dict:
        curNode = root
        for letter in word.lower():
            if 97 <= ord(letter) < 123:
                nextNode = curNode.children[ord(letter)-97]
                if nextNode is None:
                    nextNode = TrieNode(curNode, letter)
                    curNode.hasChildren = True
                curNode = nextNode
        curNode.isWord = True
    return root

def searchTrie(word):
    isThere = False
    curNode = root
    for letter in word.lower():
        if 97 <= ord(letter) < 123:
            nextNode = curNode.children[ord(letter)-97]
            if nextNode is not None:
                curNode = nextNode
            else:
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
        out = 'The longest word that you could have played was: '
    else:
        out = 'The longest words that you could have played were: '
    counter = -1
    while len(words[counter]) == len(words[-1]):
        out += '''
    ''' + str(words[counter])
        counter -= 1
    return out

def longestCorrect(correct):
    if len(correct) == 0:
        return "You didn't play any correct words."
    out = '''The longest word that you played was:
    '''
    if len(correct) == 1:
        return out + str(correct[0])
    if len(correct[len(correct)-1]) != len(correct[len(correct)-2]):
        return out + str(correct[-1])
    out = "The longest words that you played were: "
    correct = sorted(correct,key=len)
    out += '''
    ''' + str(correct[len(correct)-1])
    counter = 2
    while len(correct[len(correct)-counter+1]) == len(correct[len(correct)-counter]) and counter < len(correct) + 1:
        out += '''
    ''' + str(correct[len(correct)-counter])
        counter += 1
    return out

englishFrequency = {'A':84,'B':16,'C':29,'D':44,'E':132,'F':23,'G':21,'H':62,'I':71,'J':3,'K':9,'L':5,'M':25,'N':68,'O':77,'P':20,'Q':2,'R':61,'S':64,'T':93,'U':29,'V':11,'W':25,'X':3,'Y':21,'Z':2}
frenchFrequency = {'A':81,'B':9,'C':34,'D':37,'E':167,'F':11,'G':9,'H':7,'I':76,'J':6,'K':1,'L':55,'M':30,'N':71,'O':58,'P':25,'Q':14,'R':67,'S':79,'T':72,'U':64,'V':18,'W':1,'X':4,'Y':1,'Z':3}
germanFrequency = {'A':71,'B':19,'C':27,'D':51,'E':163,'F':17,'G':30,'H':46,'I':66,'J':3,'K':14,'L':34,'M':25,'N':98,'O':30,'P':7,'Q':1,'R':70,'S':74,'T':62,'U':52,'V':8,'W':19,'X':1,'Y':1,'Z':11}
spanishFrequency = {'A':111,'B':22,'C':40,'D':50,'E':159,'F':7,'G':18,'H':7,'I':61,'J':5,'K':1,'L':50,'M':32,'N':66,'O':86,'P':25,'Q':9,'R':68,'S':79,'T':46,'U':29,'V':11,'W':1,'X':2,'Y':10,'Z':5}

print(97 * '-' + '''
''' + 40 * ' ' + 'Welcome to Boggle''''
''' + 97 * '-' + '''

''')

print(25*'-' + ' Rules ' + 25*'-')

print('''
1. The letters must be adjoining in a 'chain'. (Letter cubes in the chain may be adjacent horizontally, vertically, or diagonally.)
2. Words must contain at least three letters.
3. No letter cube may be used more than once within a single word.
4. You have 3 minutes to find as many words as you can.
5. The longer the word, the more points you score:

Letters:	Points:
3 or 4 letters	1 point
5 letters	2 points
6 letters	3 points
7 letters	5 points
8+ letters	11 points
''')

print(25 * '-' + " Menu " + 25*'-')
print(''' 
    Choose a language: 
        1. English
        2. French
        ''')

menu = True
while menu:
    choice = input("Your Choice [1-2]:  ")
    menu = False
    if choice == '1':
        root = makeTrie("english.txt")
        letters = letterFrequency(englishFrequency)
    elif choice == '2':
        root = makeTrie("french.txt")
        letters = letterFrequency(frenchFrequency)
    #elif choice == '3':
    #    root = makeTrie("german.txt")
    #    letters = letterFrequency(germanFrequency)
    #elif choice == '4':
    #    root = makeTrie("spanish.txt")
    #    letters = letterFrequency(spanishFrequency)
    else:
        menu = True

print('''
''' + 25*'-' + " Game " + 25*'-' + '''
''')

grid = createGrid()

fullGrid = fillGrid(grid)

print(fullGrid[0])
print(fullGrid[1])
print(fullGrid[2])
print(fullGrid[3])

words = possibleWords(fullGrid)

print("There are " + str(len(words)) + " possible words.")

running = True
correct = []
score = 0

start = time.time()

while running:
    attempt = (str(input("Enter a word.  "))).upper()
    if attempt == "EXITGAME":
        running = False
        break
    if len(attempt) < 3:
        print("    Words must be at least 3 letters long.")
    elif attempt in words:
        if attempt in correct:
            print("    You have already used this word.")
        else:
            if len(attempt) == 3 or len(attempt) == 4:
                score += 1
            if len(attempt) == 5:
                score += 2
            if len(attempt) == 6:
                score += 3
            if len(attempt) == 7:
                score += 5
            if len(attempt) >= 8:
                score += 11
            correct.append(attempt)
            print("    Correct. Well done!")
            if len(correct) == len(words):
                print('''
    ''' + "Congratulations!!! You have found all of the words and completed the game!!!")
                running = False
                break
    else:
        print("    Incorrect. Try again.")
    end = time.time()
    if (end-start) >= 180:
        print('''
    ''' + "You have run out of time.")
        running = False

longestWords = longestWords(words)

longestCorrect = longestCorrect(correct)

if not running:
    print('''
''' + 25 * '-' + " Score " + 25 * '-' + '''
''')
    print("Your final score is:  " + str(score) + '''

''' + str(longestWords) + '''

''' + str(longestCorrect) + '''

    ''' + "Thank you for playing.")
