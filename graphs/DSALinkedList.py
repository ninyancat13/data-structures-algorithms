class DSAListNode:
    def __init__(self, inValue):
        self.value = inValue
        self.next = None
        self.prev = None
    
class DSALinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def getSize(self):
        return self.size

    def insertFirst(self, newValue):
        self.size += 1
        newNd = DSAListNode(newValue)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            currNd = self.head
            currNd.prev = newNd
            newNd.next = currNd 
            self.head = newNd

    def insertLast(self, newValue):
        self.size += 1
        newNd = DSAListNode(newValue)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            currNd = self.tail
            currNd.next = newNd
            newNd.prev = currNd
            self.tail = newNd

    def isEmpty(self):
        return self.head == None

    def peekFirst(self):
        nodeValue = None
        if self.isEmpty():
            raise Exception("DSALinkedList is empty")
        else:
            nodeValue = self.head.value
        return nodeValue
    
    def peekLast(self):
        nodeValue = None
        if self.isEmpty():
            raise Exception("DSALinkedList is empty")
        else:
            nodeValue = self.tail.value
        return nodeValue

    def removeFirst(self):
        nodeValue = None
        if self.isEmpty():
            raise Exception("DSALinkedList is empty")
        elif self.head.next == None:
            nodeValue = self.head.value
            self.head = None
            self.tail = None
        else:
            self.size = self.size - 1
            nodeValue = self.head.value
            self.head = self.head.next
            self.head.prev = None
        return nodeValue

    def removeLast(self):
        nodeValue = None
        if self.isEmpty():
            raise Exception("DSALinkedList is empty")
        elif self.head.next == None:
            nodeValue = self.head.value
            self.head = None
            self.tail = None
        else:
            self.size = self.size - 1
            nodeValue = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
        return nodeValue
    
    def display(self):
        currNd = self.head
        while currNd != None:
            print(currNd.value) 
            currNd = currNd.next    

    def __iter__(self):
        return DSALinkedListIterator(self)


class DSALinkedListIterator():
    def  __init__(self, theList):
        self.iterNext = theList.head
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.iterNext is None:
            raise StopIteration("Stopiteration: list is already empty")
        else:
            currVal = self.iterNext.value
            self.iterNext  = self.iterNext.next
        return currVal

