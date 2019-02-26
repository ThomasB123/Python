import random
import time

def bogo(lst):
	start = time.time()
	done = False
	count = 0
	while not done:
		count += 1
		new = []
		check = []
		for x in lst:
			check.append(x)
		minus = 0
		for x in range(len(lst)):
			minus += 1
			add = check.pop(random.randint(0,len(lst)-minus))
			new.append(add)
		if sorted(lst) == new:
			end = time.time()
			taken = end-start
			print("took",taken,"seconds to sort")
			print("tried",count,"random permutations")
			poss = 10*9*8*7*6*5*4*3*2
			print("out of a possible",poss,"permutations")
			return new,"is sorted"

lst = [6,3,89,2,7,3,6,8,4,45]
print(bogo(lst))