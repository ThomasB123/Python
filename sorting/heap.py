def Heapify(A,v,n):
    # n is heap size
    # find largest among v and 2v (left child)
    largest = v
    if 2*v <= n and A[2*v] > A[v]:
        largest = 2*v
    # find largest among winner above and 2v+1 (right child)
    if 2*v+1 <= n and A[2*v+1] > A[largest]:
        largest = 2*v+1
    if largest != v:
        A[v], A[largest] = A[largest] , A[v]
        Heapify(A,largest,n)

def HeapSort(A):
    HeapSize = len(A)
    # build heap
    for i in range(HeapSize-1,-1,-1):
        Heapify(A,i,HeapSize-1)
    for i in range(len(A)-1,0,-1):
        A[i],A[0] = A[0],A[i]
        HeapSize = HeapSize-1
        Heapify(A,0,HeapSize-1)

A = [6,1,10,8,3,7,2,4,9,5,20,34,63,3,21,19,15,25]
HeapSort(A)
print(A)