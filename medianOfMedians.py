import random
import time

def median_of_medians(A,i):
	if len(A) <= 5:
		A.sort()
		return A[i]
	num_groups = len(A)//5 if len(A) % 5 == 0 else 1+len(A)//5
	medians = []
	for j in range(num_groups):
		slice = A[j*5:min(j*5+5,len(A))]
		slice.sort()
		medians = medians + [slice[len(slice)//2]]
	x = median_of_medians(medians,len(medians)//2)
	low = []
	high = []
	for e in A:
		if e < x:
			low = low + [e]
		elif e > x:
			high = high + [e]
	k = len(low)
	if i < k:
		return median_of_medians(low,i)
	elif i > k:
		return median_of_medians(high,i-(k+1))
	return x

start = time.time()
for i in range(10):
	A = []
	for x in range(50000):
		A.append(x)
	random.shuffle(A)
	i = random.randint(0,50000-1)
	x = median_of_medians(A,i)
	'''
	if x == i:
		print("i=%d OK" %i)
	else:
		print("i=%d something is wrong" %i)
	'''
end = time.time()
print(end-start)

def median_of_medians(A,i):
	if len(A) <= 5:
		return sorted(A)[i]
	x = select(A)
	k = -1
	for j in range(len(A)):
		if A[j] < x:
			k += 1
			A[k],A[j] = A[j],A[k]
	k += 1
	A[k],A[-1] = A[-1],A[k]
	if i == k-1:
		return x-1
	elif i < k-1:
		return median_of_medians(A[:k],i)
	else:
		return median_of_medians(A[k:],i-k)

def select(A):
	if len(A) == 1:
		return A[0]
	medians = []
	group = []
	x = 0
	while x < len(A):
		if len(group) < 5:
			group.append(A[x])
			x += 1
		else:
			medians.append(sorted(group)[2])
			group = []
	medians.append(sorted(group)[int(len(group)/2)])
	return select(medians)

start = time.time()
for i in range(10):
	A = []
	for x in range(50000):
		A.append(x)
	random.shuffle(A)
	i = random.randint(0,50000-1)
	x = median_of_medians(A,i)
	'''
	if x == i:
		print("i=%d OK" % i)
	else:
		print("i=%d something is wrong" % i)
	'''
end = time.time()
print(end-start)
