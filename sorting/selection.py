### Selection Sort ###

# Regular selection sort
def selection(lst):
	for i in range(len(lst)-1):
		elem = lst[i]
		pos = i
		for j in range(i+1,len(lst)):
			if lst[j] < elem:
				elem = lst[j]
				pos = j
		lst[i] , lst[pos] = lst[pos] , lst[i]
	return lst

lst = [6,3,89,2,7,3,6,8,4,45]
print(lst)
selection(lst)
print(lst)

# Annotated version of selection sort
def selection2(lst):
	for i in range(len(lst)-1):
		elem = lst[i]
		pos = i
		for j in range(i+1,len(lst)):
			if lst[j] < elem: # change this inequality to sort descending
				elem = lst[j]
				pos = j
		print("the smallest item left is " + str(lst[pos]))
		print("so swap it with " + str(lst[i]))
		lst[i] , lst[pos] = lst[pos] , lst[i]
		print("so now the list looks like this " + str(lst))
	return lst

lst = [6,3,89,2,7,3,6,8,4,45]
print(lst)
selection2(lst)
print(lst)