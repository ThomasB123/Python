### Minesweeper ###

import random

'''
u - unexplored
e - explored
m - mine
n - no mine
'''

board = []
for x in range(10):
	add = []
	for x in range(10):
		add.append(['u','n'])
	board.append(add)
#print(board)

for i in range(10):
	board[random.randint(0,9)][random.randint(0,9)][1] = 'm'

for x in board:
	print(x)