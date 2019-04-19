from DSALinkedList import *
from ll_stacks_queues import *

#Use two classes: graph vertex and graph. Linked list will be stored within each vertex, which itself is also a vertex.
class GraphVertex():
    def __init__(self, label, value):
        self.label = label
        self.value = value
        self.links = DSALinkedList()
        self.visited = False

    def __str__(self):
        print(self.label, self.value)

    def addEdge(self, vertex2):
        self.links.insertLast(vertex2)

    def displayAdjList(self):
        print(self.label + ": ", end = "")
        for v in self.links:
            print(v.label, end = " ")

    def haveEdge(self, cv):
        found = False
        for v in self.links:
            if v == cv:
                found = True
        return found


class Graph():
    def __init__(self, filename=None):
        self.vertices = DSALinkedList()
        if filename:
            self.readGraph(filename)

# To read graph from the files provided.
    def readGraph(self, filename):
        readfile = open(filename)
        lines = readfile.readlines()
        for line in lines:
            label1 = line.split()[0]
            value1 = label1 + "_VALUE"
            label2 = line.split()[1]
            value2 = label2 + "_VALUE"
            vertex1 = self.findVertex(label1)
            vertex2 = self.findVertex(label2)
            if not vertex1:
                self.addVertex(label1, value1)
                vertex1 = self.findVertex(label1)
            if not vertex2:
                self.addVertex(label2, value2)
                vertex2 = self.findVertex(label2)
            self.addEdgeV(vertex1, vertex2)

    def addVertex(self, label, value):
        newNode = GraphVertex(label, value)
        #newNode = GraphVertex(value, label1)
        self.vertices.insertLast(newNode)

    def findVertex(self, label):
        match = None
        for v in self.vertices:
            if v.label == label:
                match = v
        return match

    def addEdge(self, label1, label2):
        vertex1 = self.findVertex(label1)
        vertex2 = self.findVertex(label2)
        vertex1.addEdge(vertex2)
        vertex2.addEdge(vertex1)

    def addEdgeV(self, vertex1, vertex2):
        vertex1.addEdge(vertex2)
        vertex2.addEdge(vertex1)

    def display(self):
        for v in self.vertices:
            print(v.label, v.value)

#Display using the adjacency matrix...
    def displayAdjList(self):
        for v in self.vertices:
            v.displayAdjList()
            print()

#Display using the adjacency matrix...
    def displayAdjMatrix(self):
        for cv in self.vertices:
            for rv in self.vertices:
                if rv.haveEdge(cv):
                    print("1", end = " ")
                else:
                    print("0", end = " ")
            print()

#Depth first uses a stack strucutre
    def depthFirstSearch(self):
        self.clearVisited()
        T = DSALinkedList()
        S = DSAStack()
        v = self.vertices.peekFirst()
        #Must show whether it was visited first before going to next node
        v.visited = True
        S.push(v)
        T.insertLast(v.label)
        #print("Vertex: " + v.label)
        self.depthFirstSearchRecursive(v, S, T)
        T.display()
        self.clearVisited()

    def depthFirstSearchRecursive(self, vertex1, stack, ll):
        if not stack.isEmpty():
            for vertex2 in vertex1.links:
                if vertex2.visited == False:
                    #print("Vertex: " + vertex2.label)
                    ll.insertLast(vertex2.label)
                    vertex2.visited = True
                    stack.push(vertex2)
                    self.depthFirstSearchRecursive(vertex2, stack, ll)
            stack.pop()

#Breadth uses a queue structure...
    def breadthFirstSearch(self):
        self.clearVisited()
        T = DSALinkedList()
        Q = DSAQueue()
        v = self.vertices.peekFirst()
        v.visited = True
        Q.enqueue(v)

        T.insertLast(v.label)
        while not Q.isEmpty():
            for w in v.links:
                if w.visited == False:
                    #T.insertLast(v.label + ',' + w.label)
                    T.insertLast(w.label)
                    w.visited = True
                    Q.enqueue(w)
            v = Q.dequeue()
        T.display()

#Must clear all visited at the very end of the code
    def clearVisited(self):
        for i in self.vertices:
            i.visited = False
