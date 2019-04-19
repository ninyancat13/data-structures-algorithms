import numpy as np
from DSALinkedList import *

class DSAStack():

    def __init__(self):
        self.count = 0
        self.stack = DSALinkedList()

    def getCount(self):
        return self.count

    def isEmpty(self):
        return self.stack.isEmpty()

    def push(self, data):
        self.stack.insertFirst(data)

    def pop(self):
        topVal = self.stack.removeFirst()
        return topVal

    def top(self):
        topVal = -1
        topVal = self.stack.peekFirst()
        return topVal

    def iterator(self):
        return self.stack.__iter__()

class DSAQueue():

    def __init__(self):
        self.count = 0
        self.queue = DSALinkedList()

    def getCount(self):
        return self.count

    def isEmpty(self):
        return self.queue.isEmpty()

    def enqueue(self, data):
        self.queue.insertLast(data)

    def dequeue(self):
        frontVal = self.queue.removeFirst()
        return frontVal

    def peek(self):
        frontVal = -1
        frontVal = self.queue.peekFirst()
        return frontVal

    def iterator(self):
        return self.queue.__iter__()
