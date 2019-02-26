from pygame_functions import *
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

def fillRandomGrid(randomGrid):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for x in range(len(randomGrid)):
        for y in range(len(randomGrid[x])):
            randomGrid[x][y] = alphabet[random.randint(0,25)]
    return randomGrid

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

def translateRandom(list):
    word = ''
    for x in range(len(list)):
        word += fullRandomGrid[list[x][0]][list[x][1]]
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
    for x in range(len(fullGrid)):
        for y in range(len(fullGrid[x])):
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

def possibleRandomWords(fullRandomGrid):
    possible = []
    queue = []
    for x in range(len(fullRandomGrid)):
        for y in range(len(fullRandomGrid[x])):
            queue.append([[x,y]])
    while len(queue) > 0:
        current = queue[0]
        stub = translateRandom(current)
        if searchStub(stub):
            neighbours = validNeighbours(current[-1][0], current[-1][1])
            for a in range(len(neighbours)):
                add = []
                if neighbours[a] not in current:
                    for b in range(len(current)):
                        add.append(current[b])
                    add.append(neighbours[a])
                    if searchStub(translateRandom(add)):
                        queue.append(add)
            if searchTrie(stub) and stub not in possible:
                possible.append(stub)
        del queue[0]
    return possible


englishFrequency = {'A':84,'B':16,'C':29,'D':44,'E':132,'F':23,'G':21,'H':62,'I':71,'J':3,'K':9,'L':5,'M':25,'N':68,'O':77,'P':20,'Q':2,'R':61,'S':64,'T':93,'U':29,'V':11,'W':25,'X':3,'Y':21,'Z':2}
frenchFrequency = {'A':81,'B':9,'C':34,'D':37,'E':167,'F':11,'G':9,'H':7,'I':76,'J':6,'K':1,'L':55,'M':30,'N':71,'O':58,'P':25,'Q':14,'R':67,'S':79,'T':72,'U':64,'V':18,'W':1,'X':4,'Y':1,'Z':3}


randomGrid = createGrid()
grid = createGrid()

global letters
global root

letters = letterFrequency(frenchFrequency)
root = makeTrie("french.txt")

for x in range(50):
    fullRandomGrid = fillRandomGrid(randomGrid)
    fullGrid = fillGrid(grid)
    randomWords = possibleRandomWords(fullRandomGrid)
    words = possibleWords(fullGrid)
    print(str(len(randomWords)) + '   ' + str(len(words)))






