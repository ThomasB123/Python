### Quick Sort ###

# Regular, efficient version, no annotations
def quick(A,left,right):
	if left < right:
		pivot = partition(A,left,right)
		quick(A,left,pivot-1)
		quick(A,pivot+1,right)

def partition(A,left,right):
	x = A[right]
	i = left - 1
	for j in range(left,right):
		if A[j] < x:
			i += 1
			A[i] , A[j] = A[j] , A[i]
	A[i+1] , A[right] = A[right] , A[i+1]
	return i + 1

lst = [6,3,89,2,7,3,6,8,4,45,5]
print(lst)
quick(lst,0,len(lst)-1)
print(lst)

# Annotated version
def quick2(A,left,right):
	if left < right:
		pivot = partition2(A,left,right)
		print("pivot is " + str(A[pivot]))
		print("left section is " + str(A[left:pivot]))
		print("right section is " + str(A[pivot+1:right+1]))
		quick2(A,left,pivot-1)
		quick2(A,pivot+1,right)

def partition2(A,left,right):
	x = A[right]
	i = left - 1
	print("pivot is " + str(x))
	for j in range(left,right):
		print("comparing " + str(A[j]) + " with the pivot")
		if A[j] < x:
			print(str(A[j]) + " is smaller so it goes to the left of the pivot")
			i += 1
			A[i] , A[j] = A[j] , A[i]
		else:
			print(str(A[j]) + " is bigger so it goes to the right of the pivot")
	A[i+1] , A[right] = A[right] , A[i+1] # putting the pivot in the correct place,
										# with numbers smaller and larger than it
										# on the left and right, respectively
	print("list is now: " + str(A))
	return i + 1

lst = [6,3,89,2,7,3,6,8,4,45,5]
print(lst)
quick2(lst,0,len(lst)-1)
print(lst)
