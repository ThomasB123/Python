def hybridSort(m):
	if len(m) <= 4:
		return selection(m)
	middle = len(m) // 2
	left = m[:middle]
	right = m[middle:]
	leftsorted = hybridSort(left)
	rightsorted = hybridSort(right)
	return merge(leftsorted, rightsorted)

def merge(left,right):
	out = []
	while len(left) > 0 or len(right) > 0:
		if len(left) > 0 and len(right) > 0:
			if left[0] >= right[0]: # descending
				out.append(left[0])
				left.pop(0)
			else:
				out.append(right[0])
				right.pop(0)
		elif len(left) > 0:
			for x in left:
				out.append(x)
			left = []
		else:
			for x in right:
				out.append(x)
			right = []
	return out

def selection(lst):
	for i in range(len(lst)-1):
		elem = lst[i]
		pos = i
		for j in range(i+1,len(lst)):
			if lst[j] > elem: # descending
				elem = lst[j]
				pos = j
		lst[i] , lst[pos] = lst[pos] , lst[i]
	return lst

lst = [6,3,89,2,7,3,6,8,4,45]
print(lst)
print(hybridSort(lst))


# Annotated version of merge sort

# Halves the list recursively
# Then calls merge function on two lists
def hybridSort2(m):
	print("now running the hybridSort function")
	if len(m) <= 4:
		print("now passing the list", m ,"to selection")
		return selection2(m)
	middle = len(m) // 2
	left = m[:middle]
	right = m[middle:]
	print("left half:" , left)
	print("right half:" , right)
	leftsorted = hybridSort2(left)
	rightsorted = hybridSort2(right)
	return merge2(leftsorted, rightsorted)

# Merges two lists together into the correct order
def merge2(left,right):
	print("now running the merge function")
	out = []
	while len(left) > 0 or len(right) > 0:
		print("left:" , left)
		print("right:" , right)
		if len(left) > 0 and len(right) > 0:
			print("comparing" , left[0] ,  "and" , right[0])
			if left[0] <= right[0]: # change this inequality to descending
				print(left[0] , "is smaller")
				out.append(left[0])
				left.pop(0)
			else:
				print(right[0] , "is smaller")
				out.append(right[0])
				right.pop(0)
			print("so add it to the sorted list:" , out)
			print("left is now" , left)
			print("right is now" , right)
		elif len(left) > 0:
			print("there is nothing in right")
			print("so add everything from left:" , left)
			print("to the sorted list:" , out)
			for x in left:
				out.append(x)
			left = []
		else: # len(right) > 0
			print("there is nothing in left")
			print("so add everything from right:" , right)
			print("to the sorted list:" , out)
			for x in right:
				out.append(x)
			right = []
		print("out is now" , out)
	print("so the merge of the two lists is" , out)
	return out

# Annotated version of selection sort
def selection2(lst):
	for i in range(len(lst)-1):
		elem = lst[i]
		pos = i
		for j in range(i+1,len(lst)):
			if lst[j] < elem: # change this inequality to sort descending
				elem = lst[j]
				pos = j
		print("the smallest item left is" , lst[pos])
		print("so swap it with" , lst[i])
		lst[i] , lst[pos] = lst[pos] , lst[i]
		print("so now the list looks like this" , lst)
	return lst

lst = [6,3,89,2,7,3,6,8,4,45]
print(lst)
print(hybridSort2(lst))
