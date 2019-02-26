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
    root = TrieNode(None, '')
    for word in dict:
        curNode = root
        for letter in word.lower():
            if 97 <= ord(letter) < 123:
                nextNode = curNode.children[ord(letter)-97]
                if nextNode is None:
                    nextNode = TrieNode(curNode, letter)
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



grid = createGrid()

global letters
global root

letters = letterFrequency(frenchFrequency)
root = makeTrie("french.txt")

fullGrid = fillGrid(grid)
words = possibleWords(fullGrid)

print(words)
print(longestWords(words))

endWait()