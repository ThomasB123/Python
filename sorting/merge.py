### Merge Sort ###

def mergeSort(m):
	if len(m) <= 1:
		return m
	middle = len(m) // 2
	left = m[:middle]
	right = m[middle:]
	leftsorted = mergeSort(left)
	rightsorted = mergeSort(right)
	return merge(leftsorted, rightsorted)

def merge(left,right):
	out = []
	while len(left) > 0 or len(right) > 0:
		if len(left) > 0 and len(right) > 0:
			if left[0] <= right[0]:
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

lst = [6,3,89,2,7,3,6,8,4,45]
print(lst)
print(mergeSort(lst))

# Annotated version of merge sort

# Halves the list recursively
# Then calls merge function on two lists
def mergeSort2(m):
	print("now running the mergeSort function")
	if len(m) <= 1:
		return m
	middle = len(m) // 2
	left = m[:middle]
	right = m[middle:]
	print("left half: " + str(left))
	print("right half: " + str(right))
	leftsorted = mergeSort2(left)
	rightsorted = mergeSort2(right)
	return merge2(leftsorted, rightsorted)

# Merges two lists together into the correct order
def merge2(left,right):
	print("now running the merge function")
	out = []
	while len(left) > 0 or len(right) > 0:
		print("left: " + str(left))
		print("right: " + str(right))
		if len(left) > 0 and len(right) > 0:
			print("comparing " + str(left[0]) +  " and " + str(right[0]))
			if left[0] <= right[0]: # change this inequality to make descending
				print(str(left[0]) + " is smaller")
				out.append(left[0])
				left.pop(0)
			else:
				print(str(right[0]) + " is smaller")
				out.append(right[0])
				right.pop(0)
			print("so add it to the sorted list: " + str(out))
			print("left is now " + str(left))
			print("right is now " + str(right))
		elif len(left) > 0:
			print("there is nothing in right")
			print("so add everything from left: " + str(left))
			print("to the sorted list: " + str(out))
			for x in left:
				out.append(x)
			left = []
		else: # len(right) > 0
			print("there is nothing in left")
			print("so add everything from right: " + str(right))
			print("to the sorted list: " + str(out))
			for x in right:
				out.append(x)
			right = []
		print("out is now " + str(out))
	print("so the merge of the two lists is " + str(out))
	return out

lst = [6,3,89,2,7,3,6,8,4,45]
print(lst)
print(mergeSort2(lst))
