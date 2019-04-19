import numpy as np

class DSAHashEntry():
    def __init__(self, inKey="", inValue=None, state=0):
        self.key = inKey
        self.value = inValue
        self.state = state

class DSAHashTable():
    def __init__ (self, capacity=10):
        self.actualSize = self.nextPrime(capacity)
        self.table = np.empty(self.actualSize, dtype=object)
        for ii in range (0, self.actualSize):
            self.table[ii] = DSAHashEntry()
        self.counter = 0
    
    def put(self, inKey, inValue):
        hashIdx = self.hash2(inKey)
        origIdx = hashIdx
        found = False
        giveUp = False
        
        while not found and not giveUp:
            if (self.table[hashIdx].state <= 0):
                found = True
            elif (self.table[hashIdx].key == inKey):
                print("Duplicate Key")
                giveUp = True
            else:
                hashIdx = (hashIdx + 1)% self.actualSize
                if hashIdx == origIdx: 
                    giveUp = True
        
        if found:
            self.table[hashIdx] = DSAHashEntry(inKey, inValue, state = 1)      
            print(inKey, inValue, origIdx, hashIdx)
            self.counter = self.counter + 1
            loadFactor = self.counter // self.actualSize 
            if loadFactor > 0.7:
                self.resize(self.actualSize * 2)

    def get(inKey):
        hashIdx = self.hash2(inKey)
        origIdx = hashIdx
        found = False
        giveUp = False

        while not found and not giveUp:
            if (self.table[hashIdx].state == 0):
                giveUp = True
            elif (self.table[hashIdx].key == inKey):
                found = True
            else:
                hashIdx = (hashIdx + 1)% self.actualSize
                if hashIdx == origIdx: 
                    giveUp = True
        
        if not found:
            retValue = self.table[hashIdx].value      

    def nextPrime(self,startVal):
        if startVal % 2 == 0 :
            primeVal = startVal -1
        else:
            primeVal = startVal
        
        isPrime = False
        while not isPrime:    
            primeVal = primeVal + 2
            ii = 3
            isPrime = True
            rootVal = (primeVal)**(0.5) 
        
            while ii <= rootVal and isPrime:
                if primeVal % ii == 0 :
                    isPrime = False
                else:
                    ii = ii + 2
        return primeVal

    def display(self):
        for i in range(self.actualSize):
            print(self.table[i].key, self.table[i].value, self.table[i].state)

    def remove(self,inKey):
        hashIdx = self.hash2(inKey)
        origIdx = hashIdx
        found = False
        giveUp = False

        while not found and not giveUp:
            if (self.table[hashIdx].state == 0):
                giveUp = True
            elif (self.table[hashIdx].key == inKey):
                found = True
            else:
                hashIdx = (hashIdx + 1)% self.actualSize
                if hashIdx == origIdx: 
                    giveUp = True
        if found:
            self.table[hashIdx].key = None
            self.table[hashIdx].value = None
            self.table[hashIdx].state = -1
            self.counter = self.counter - 1 
            loadFactor = self.counter // self.actualSize 
            print("Delete")    
            if loadFactor < 0.2:
                self.resize(int(self.actualSize / 2))

    def resize(self,size):
        newcapacity = self.nextPrime(size)
        print("Resizing from", self.actualSize, " to ", newcapacity)
        newTable = np.empty(newcapacity, dtype=object)
        self.actualSize = newcapacity
        for ii in range (0, newcapacity):
            newTable[ii] = DSAHashEntry()
        oldTable = self.table
        self.table = newTable
        for jj in range (len(oldTable)):
            if oldTable[jj].state == 1:
                self.put(oldTable[jj].key, oldTable[jj].value)

    def hash2(self, inKey):
        a = 63689
        b = 378551
        hashIdx = 0

        for ii in range(0, len(inKey)):
            hashIdx = (hashIdx * a) + ord(inKey[ii])
            a *= b
        #print(hashIdx, self.actualSize)        
        return hashIdx % self.actualSize 
 
 
    def save(self):
        fo = open("File_Input_RandomNames.csv", "w")
        for jj in range (len(self.table)):
            if self.table[jj].state == 1:
                fo.write(str(self.table[jj].key) + "," + str(self.table[jj].value)+ '\n')
        fo.close()
