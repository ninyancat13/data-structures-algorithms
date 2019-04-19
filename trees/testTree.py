from tree import *
import pickle

myTree = BinarySearchTree()

myTree.displayInOrder()

myTree.insert(5, "five")
myTree.insert(6, "six")
myTree.insert(3, "three")
myTree.insert(8, "eight")
myTree.insert(2, "two")
myTree.insert(9, "nine")
myTree.insert(7, "seven")

print("\nPrint these in in order...")
inOrder = myTree.displayInOrder()
#inOrder

print("\nPrint these in pre order...")
preOrder = myTree.displayPreOrder()
#preOrder

print("\nPrint these in post order...")
postOrder = myTree.displayPostOrder()
#postOrder



print("Find 9...")
print(myTree.find(9))

print("Delete 9...")
print(myTree.delete(9))

print("Now display this tree again in order...")
myTree.displayInOrder()

print("What is the height of the tree?")
print(myTree.height())
