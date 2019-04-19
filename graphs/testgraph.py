#Test the graph code

from graph import *

g = Graph()
# g is the graph from graph.py
g.addVertex('a', 'A')
g.addVertex('b', 'B')
g.addVertex('c', 'C')
g.addVertex('d', 'D')
g.addVertex('e', 'E')

#now add the edges
g.addEdge('a', 'b')
g.addEdge('c', 'a')
g.addEdge('b', 'c')
g.addEdge('d', 'a')
g.addEdge('d', 'c')
g.addEdge('e', 'a')
g.addEdge('e', 'd')
g.addEdge('e', 'b')

print("\nDisplay the entire graph...\n")
g.display()

print("\nDisplay the adjacency matrix...\n")
g.displayAdjMatrix()

print("\nDisplay the adjacency list...\n")
g.displayAdjList()

print("\nUse the breadth First Search on the graph...\n")
g.breadthFirstSearch()

print("\nUse the Depth First Search on the graph...\n")
g.depthFirstSearch()


print("\n\n\nNow we will try to display the Prac6_1.al FILE\n")
g1 = Graph(filename = "prac6_1.al")
print("\nDisplay the adjacency list...\n")
g1.displayAdjList()
print("\nDisplay the adjacency matrix...\n")
g1.displayAdjMatrix()
print("\nNow apply depth first search...\n")
g1.depthFirstSearch()
print("\nNow apply breadth first search...\n")
g1.breadthFirstSearch()

print("\n\n\nNow we will try to display the Prac6_2.al FILE\n")
g2 = Graph(filename="prac6_2.al")
print("\nDisplay the adjacency list...\n")
g2.displayAdjList()
print("\nDisplay the adjacency matrix...\n")
g2.displayAdjMatrix()
print("\nNow apply depth first search...\n")
g2.depthFirstSearch()
print("\nNow apply breadth first search...\n")
g2.breadthFirstSearch()

