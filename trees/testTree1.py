from tree import *
import pickle
from ll_stacks_queues import *

myTree = BinarySearchTree()

myTree.displayInOrder()

fileobj = open("randomnames.csv")
lines = fileobj.readlines()

for line in lines:
    linesplit = line.split(",")
    if linesplit[0] != None:
        myTree.insert(linesplit[1], linesplit[0])
    else:
        break

print("\nPrint these in in order...")
inOrder = myTree.displayInOrder()
inOrder

print("\nPrint these in pre order...")
preOrder = myTree.displayPreOrder()
preOrder

print("\nPrint these in post order...")
postOrder = myTree.displayPostOrder()
postOrder


keyQueue = DSAQueue()
valueQueue = DSAQueue()

print("Now let us try traversing in inOrder")
traverseInOrder1 = myTree.traverseInOrder(keyQueue, valueQueue)
print(traverseInOrder1)


print("Now let us try traversing in preOrder")


print("Now let us try traversing in postOrder")


#pickle.dump(inOrder, open("inOrder.bin", "wb"))
#pickle.load(open("inOrder.bin", "rb"))
#
#pickle.dump(preOrder, open("preOrder.bin", "wb"))
#pickle.load(open("preOrder.bin", "rb"))
#
#pickle.dump(postOrder, open("postOrder.bin", "wb"))
#pickle.load(open("postOrder.bin", "rb"))
