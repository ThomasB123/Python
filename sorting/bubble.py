### Bubble Sort ###

# More efficient version of bubble sort
def bubble(lst):
	for i in range(len(lst)-1):
		swaps = 0
		for j in range(len(lst)-i-1):
			if lst[j] > lst[j+1]:
				lst[j] , lst[j+1] = lst[j+1] , lst[j]
				swaps += 1
		if swaps == 0:
			return lst

lst = [6,3,89,2,7,3,6,8,4,45]
print(lst)
bubble(lst)
print(lst)

# Most inefficient version of bubble sort
def inefficient(lst):
	for i in range(len(lst)-1):
		for j in range(len(lst)-1):
			if lst[j] > lst[j+1]:
				lst[j] , lst[j+1] = lst[j+1] , lst[j]
	return lst


#Annotated version of bubble sort
def bubble2(lst):
	print("initial list: "+str(lst))
	total = 0
	comparisons = 0
	for i in range(len(lst)-1):
		swaps = 0
		for j in range(len(lst)-i-1): #in less efficient version this is len(lst)-1
			print(lst)
			print("comparing " + str(lst[j]) + " and " + str(lst[j+1]))
			comparisons += 1
			if lst[j] > lst[j+1]:
				print("swapping")
				lst[j] , lst[j+1] = lst[j+1] , lst[j]
				swaps += 1
				total += 1
			else:
				print("no swap")
		if swaps == 0:
			print("sorted list " + str(lst))
	print(str(comparisons) + " comparisons were made")
	print(str(total) + " swaps were made")

lst = [6,3,89,2,7,3,6,8,4,45]
bubble2(lst)