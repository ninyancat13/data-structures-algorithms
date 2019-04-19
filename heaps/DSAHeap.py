CAPACITY = 7000

class DSAHeap():

    def __init__(self):
        self.heapArr = [0]*CAPACITY
        self.heap_size = 0

    def add(self, item):
        if CAPACITY == self.heap_size:
            return
        self.heapArr[self.heap_size] = item
        self.heap_size = self.heap_size + 1
        self.trickleUp(self.heap_size-1)

    def remove(self):
        value = self.heapArr[0]
        #self.swap(0, self.heap_size-1)
        self.heapArr[0] = self.heapArr[-1]
        self.heapArr[-1] = None
        self.trickleDown(0)
        self.heap_size = self.heap_size - 1
        return value

    def size(self):
        print(self.heap_size)

    def get_max(self):
        return self.heapArr[0]

    def swap(self, index1, index2):
        self.heapArr[index2], self.heapArr[index1] = self.heapArr[index1], self.heapArr[index2]

# can either do iteratively or recursively. For trickleup, I have used iteration.
    def trickleUp(self, curIdx):
        parentIdx = (curIdx - 1)//2
        while curIdx > 0 and self.heapArr[curIdx] > self.heapArr[parentIdx]:
            temp = self.heapArr[parentIdx]
            self.heapArr[parentIdx] = self.heapArr[curIdx]
            self.heapArr[curIdx] = temp
            curIdx = parentIdx
            parentIdx = (curIdx - 1)//2
        return self.heapArr

# for trickleDown, recursive method was implemented!
    def trickleDown(self, curIdx):
        lChildIdx = curIdx * 2 + 1
        rChildIdx = lChildIdx + 1
        index_largest = curIdx

        if lChildIdx < self.heap_size and self.heapArr[lChildIdx] > self.heapArr[curIdx]:
            index_largest = lChildIdx

        if rChildIdx < self.heap_size and self.heapArr[rChildIdx] > self.heapArr[index_largest]:
            index_largest = rChildIdx

        if curIdx != index_largest:
            self.swap(curIdx, index_largest)
            self.trickleDown(index_largest)

    def heapify(self):
        max = self.get_max()
        self.swap(0, self.heap_size-1)
        self.heap_size = self.heap_size - 1
        self.trickleDown(0)
        return max

    def heapSort(self):
        size = self.heap_size

        for ii in range(0, size):
            max = self.heapify()
            print(max)

