#######
#NODES#
#######
class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

########
#STACKS#
########

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data

########
#QUEUES#
########

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def dequeue(self):
        output = self.front.data
        self.front = self.front.after
        if self.front == None:
            self.rear = None
        return output
    def enqueue(self, data):
        if self.rear == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear.after = Node(data, self.rear)
            self.rear = self.rear.after

#####################################################


def testq3():
    assert good_expression("1+2+3+4")
    assert not good_expression("(1+2+3+4)")
    assert good_expression("(1+2)*3+4")
    assert not good_expression("((1+2))*3+4")
    assert good_expression("1+2*3+4")
    assert not good_expression("1+(2*3)+4")
    assert good_expression("1*2+3+4")
    assert not good_expression("1*2+(3+4)")
    print ("all tests passed")

#####################################################
