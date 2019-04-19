import numpy as np
from DSALinkedList import *

class DSAStack():

    def __init__(self, max_capacity=100):
        self.capacity = max_capacity
        self.stack = np.zeros(max_capacity, dtype=object)
        print(self.stack)
        self.count = 0

    def getCount(self):
        return self.count

    def isEmpty(self):
        if self.count == 0:
           return True
        else:
           return False
        #return self.count == 0
    
    def isFull(self):
        if self.count == self.capacity:
            return True and self.capacity
        else:
            return False
        #return self.count == self.capacity

    def push(self,value):
        if self.isFull():
            raise StackOverflowError("Stack is full")
        else:
            self.stack[self.count] = value
            self.count = self.count + 1

    def pop(self):
        if self.isEmpty():
            raise StackUnderflowError("Stack is underfull")
        else:
            data =self.stack[self.count - 1]
            self.stack[self.count - 1] = 0
            self.count = self.count - 1
            return data

        topVal = self.top()
        self.count = self.count - 1
        return topVal

    def top(self):
        topVal = -1
        if self.isEmpty():
            raise StackUnderflowError("Stack is already empty")
        else:
            temp = self.count
            topVal = self.stack[temp -1]
        return topVal

    def precedenceOfTop(self):
       topVal = -2
       if self.isEmpty():
            raise StackUnderflowError("Stack is already empty")
       else:
            temp = self.count
            topVal = self.stack[temp - 2]
       return topVal

#    def ParseNextTerm(self):


    def display(self):
        print(self.stack)
                
class DSAQueue():

    queue = DSALinkedList()

    def __init__(self, max_capacity=100):
        self.capacity = max_capacity
        self.queue = np.zeros(self.capacity, dtype=object)
        print(self.queue)
        self.count = 0

    def getCount(self):
        return self.count

    def isEmpty(self):
        return queue.isEmpty()

    def isFull(self):
        if self.count == self.capacity:
            full = True
        else:
            full = False
        return full

    def enqueue(self, data):
        if self.isFull():
            raise QueueOverflowError("Queue is full")
        else:
            queue.insertLast(data)

    def dequeue(self):
        if self.isEmpty():
            raise QueueUnderflowError("Queue is already empty")
        else:
            frontVal = queue.removeFirst()
        return frontVal

    def peek(self):
        frontVal = -1
        if self.isEmpty():
            raise QueueUnderflowError("Queue is already empty")
        else:
            frontVal = queue.peekFirst()
        return frontVal

    def sizeQueue(self):
        return len(self.queue)
    
    def display(self):
        print(self.queue)

    def iterator(self):
        return queue.__iter__()

class Error(Exception):
    pass

class StackOverflowError(Error):
    """Exception raised if stack is overfull.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message

class StackUnderflowError(Error):
    """Exception raised if stack is underfull.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message
