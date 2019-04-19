class TreeNode(object):
    def __init__(self, inKey, inValue):
        if inKey is None:
            raise EmptyKeyTreeError("Key cannot be empty")
        self._key = inKey
        self._value = inValue
        self._leftChild = None
        self._rightChild = None

    def min(self):
        return self._minRec(self.root)._key

    def _minRec(self, currNd):
        minNode = currNd
        if currNd._leftChild != None:
            minNode = self._minRec(currNd._leftChild)
        return minNode

    def max(self):
        return self._maxRec(self.root)._key

    def _maxRec(self, currNd):
        maxNode = currNd
        if currNd._rightChild != None:
            maxNode = self._maxRec(currNd._rightChild)
        return maxNode

class BinarySearchTree(object):
    
    def __init__(self):
        self.root = None
        self.size = 0
        return

    def inOrderRec(self, currNd):
        if currNd != None:
            if currNd._leftChild != None:
                self.inOrderRec(currNd._leftChild)
            print(currNd._key, "->", currNd._value)
            if currNd._rightChild != None:
                self.inOrderRec(currNd._rightChild)

    def preOrderRec(self, currNd):
        if currNd != None:
            print(currNd._key, "->", currNd._value)
            if currNd._leftChild != None:
                self.preOrderRec(currNd._leftChild)
            if currNd._rightChild != None:
                self.preOrderRec(currNd._rightChild)
    
    def postOrderRec(self, currNd):
        if currNd != None:
            if currNd._leftChild != None:
                self.postOrderRec(currNd._leftChild)
            if currNd._rightChild != None:
                self.postOrderRec(currNd._rightChild)
            print(currNd._key, "->", currNd._value)

    def displayInOrder(self):
        self.inOrderRec(self.root)
    
    def displayPreOrder(self):
        self.preOrderRec(self.root)
    
    def displayPostOrder(self):
        self.postOrderRec(self.root)

    def find(self, inKey):
        """Find wrapper method for Binary Search Tree

        Attributes:
            key - key value to search for
        """
        return self._findRec(inKey, self.root)
    
    def _findRec(self, inKey, currNd):
        _value = None
        if currNd is None:         #Base case not found
            raise TreeError("findR", "Key not found")
        elif currNd._key == inKey:   #Base case - found
            _value = currNd._value
        elif currNd._key > inKey:    #Recurse left
            _value = self._findRec(inKey, currNd._leftChild)
        #print("Going left")
        else:                      #Recurse right
            _value = self._findRec(inKey, currNd._rightChild)
        #print("Going right")
        return _value

    def insert(self, inKey, inValue):
        """Insert wrapper method for Binary Search Tree

        Attributes:
            key - key value to search for
        """
        self.root = self.insertRec(inKey, inValue, self.root)

    def insertRec(self, inKey, inValue, currNd):
        updateNode = currNd
        if currNd == None:
            newNode = TreeNode(inKey, inValue)
            updateNode = newNode
        #print("Inserting node")
        elif currNd._key == inKey:
            raise TreeError("insertR", "Key not found")
        elif currNd._key > inKey:
            currNd._leftChild = self.insertRec(inKey, inValue, currNd._leftChild)
        #print("Going left")
        else:
            currNd._rightChild = self.insertRec(inKey, inValue, currNd._rightChild)
        #print("Going right")
        return updateNode

    def delete(self, inKey):
        return self.deleteRec(inKey, self.root)

    def deleteRec(self, inKey, currNd):
        updateNode = currNd
        if currNd == None:
            raise TreeError("Key not found")
        elif currNd._key == inKey:
            updateNode = self.deleteNode(inKey, currNd) #This might be error
        elif currNd._key > inKey:
            currNd._leftChild = self.deleteRec(inKey, currNd._leftChild)
        else:
            currNd._rightChild = self.deleteRec(inKey, currNd._rightChild)
        return updateNode

    def deleteNode(self, inKey, delNode):
        updateNode = None
        if delNode._leftChild == None and delNode._rightChild == None:
            updateNode = None
        elif delNode._leftChild is not None and delNode._rightChild == None:
            updateNode = delNode._leftChild
        elif delNode._leftChild == None and delNode._rightChild is not None:
            updateNode = delNode._rightChild
        else:
            updateNode = self.promoteSuccesor(delNode._rightChild)
            if updateNode is not delNode._rightChild:
                updateNode._rightChild = delNode._rightChild
            updateNode._leftChild = delNode._leftChild
        return updateNode

    def promoteSuccessor(self, currNd):
        successor = currNd
        if currNd._leftChild is not None:
            successor = self._promoteSuccessor(currNd._leftChild)
            if successor == currNd._leftChild:
                currNd._leftChild = successor._rightChild
        return successor

    def height(self):
        return self.heightRec(self.root)
#THIS MIGHT BE WRONG HERE

    def heightRec(self, currNd): #Do we need TreeNode inside this statement
        #What statements should be in or not in def.
        #htSoFar = None
        #iLeftHt = None
        #iRightHt = None   #THIS might not be the right formatting. How to
        #introduce the variables??
        if currNd == None:
            htSoFar = -1
        else:
            iLeftHt = self.heightRec(currNd._leftChild)
            iRightHt = self.heightRec(currNd._rightChild)

            if iLeftHt > iRightHt:
                htSoFar = iLeftHt + 1
            else:
                htSoFar = iRightHt + 1
        return htSoFar

    def traverseTree(self, currNd):
        if currNd is not None:
            self.traverseTree(currNd._leftChild)
            self.traverseTree(currNd._rightChild)

    
    def traverseInOrder(self, keyQueue, valueQueue):
        self.traverseInOrderRecursive(self.root, keyQueue, valueQueue)

    def traversePreOrder(self, keyQueue, valueQueue):
        self.traversePreOrderRecursive(self.root, keyQueue, valueQueue)

    def traversePostOrder(self, keyQueue, valueQueue):
        self.traversePostOrderRecursive(self.root, keyQueue, valueQueue)

    def traverseInOrderRecursive(self, currNd, keyQueue, valueQueue):
        if currNd != None:
            self.traverseInOrderRecursive(currNd._leftChild, keyQueue, valueQueue)
            keyQueue.enqueue(currNd._key)
            valueQueue.enqueue(currNd._value)
            self.traverseInOrderRecursive(currNd._rightChild, keyQueue, valueQueue)

    def traversePreOrderRecursive(self, currNd, keyQueue, valueQueue):
        if currNd != None:
            keyQueue.enqueue(currNd._key)
            valueQueue.enqueue(currNd._value)
            self.traversePreOrderRecursive(currNd._leftChild, keyQueue, valueQueue)
            self.traversePreOrderRecursive(currNd._rightChild, keyQueue, valueQueue)

    def traversePostOrderRecursive(self, currNd, keyQueue, valueQueue):
        if currNd != None:
            self.traversePostOrderRecursive(currNd._leftChild, keyQueue, valueQueue)
            self.traversePostOrderRecursive(currNd._rightChild, keyQueue, valueQueue)
            keyQueue.enqueue(currNd._key)
            valueQueue.enqueue(currNd._value)

#    def preorder(self, currNd):
#        res = []
#        if currNd:
#            res.append(currNd._data)
#            res = res + self.preorder(currNd._leftChild)
#            res = res + self.preorder(currNd._rightChild)
#        return res

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class TreeError(Error):
    """Exception raised for errors in tree class

    Attributes:
        method -- method in which the error occured
        message -- explanation of the error
    """

    def __init__(self, method, message):
        self.method = method
        self.message = message
