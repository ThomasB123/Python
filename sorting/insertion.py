### Insertion Sort ###

# Regular insertion sort
def insertion(lst):
	for j in range(1,len(lst)):
		x = lst[j]
		i = j - 1
		while i >= 0 and lst[i] > x:
			lst[i+1] = lst[i]
			i -= 1
		lst[i+1] = x
	return lst

lst = [6,3,89,2,7,3,6,8,4,45]
print(lst)
insertion(lst)
print(lst)

# Insertion but it prints lst throughout
def insertion2(lst):
	for j in range(1,len(lst)):
		x = lst[j]
		i = j - 1
		while i >= 0 and lst[i] > x:
			lst[i+1] = lst[i]
			i -= 1
		lst[i+1] = x
		print(i+1)
		print(lst)
	return lst

lst = [6,3,89,2,7,3,6,8,4,45]
print(lst)
insertion2(lst)
print(lst)