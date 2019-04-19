from tree import *
import pickle
from ll_stacks_queues import *
from DSALinkedList import *

selection = input("What would you like to do? (1) Write a CSV file, (2) Write serialised file,(3) Read CSV, (4) Read serialised file,(5) Display tree,(6) Exit")

myTree = BinarySearchTree() 


while selection != '6':
    #Write to CSV file THIS WORKS!!!
    if selection.upper() == '1':
        fileobj = open("randomnames.csv")
        lines = fileobj.readlines()

        for line in lines:
            linesplit = line.split(",")
            myTree.insert(linesplit[1], linesplit[0])
        #myTree.displayInOrder()

    #Write serialised file THIS WORKS!!!
    elif selection.upper() == '2':
        pickle.dump(myTree, open("tree.bin", "wb")) 
        #Unlike what we did at the start, we only dump in the myTree not the myTree.displayInOrder.
        # We are only saving the file as an object, so it is not displaying, thus it is just the
        #state of the object... later on we use displayInorder on this file to retrieve structured display
    
    #Read the CSV file THIS WORKS!!!
    elif selection.upper() == '3':
        choose = input("\nWhat CSV shall we read? Select either (A)InOrder, (B)PreOrder, (C) PostOrder, (E)xit")
        while choose != 'E':
            if choose.upper() == 'A':
                inOrder = myTree.displayInOrder()
                #inOrder
            elif choose.upper() == 'B':
                preOrder = myTree.displayPreOrder()
                #preOrder
            elif choose.upper() == 'C':
                postOrder = myTree.displayPostOrder()
                #postOrder
            choose = input("\nWhat CSV shall we read? Select either (A)InOrder, (B)PreOrder, (C) PostOrder, (E)xit")

    #Read serialised file THIS WORKS!!!
    elif selection.upper() == '4':
        choose = input("\nWhich serialisation file shall we read? Select either (A)InOrder, (B)PreOrder,(C) PostOrder, (E)xit")
        while choose != 'E':
            if choose.upper() == 'A':
                myTree = pickle.load(open("tree.bin", "rb"))
                myTree.displayInOrder()
                #myTree.insert(inOrder1[1], inOrder1[0])
                #myTree.displayInOrder()
                #inorder1.traverseInOrder()
                #qA = inorder1.displayInOrder
                #for line in inorder1:
                #    line.displayInOrder()
            elif choose.upper() == 'B':
                myTree = pickle.load(open("tree.bin", "rb"))
                myTree.displayPreOrder()
            elif choose.upper() == 'C':
                myTree = pickle.load(open("tree.bin", "rb"))
                myTree.displayPostOrder()
            choose = input("\nWhich serialisation file shall we read? Select either (A)InOrder, (B)PreOrder,(C) PostOrder, (E)xit")
   
    #Display the tree
    elif selection.upper() == '5':
        choose = input("\nWhich tree order? Select either (A)InOrder, (B)PreOrder,(C) PostOrder, (E)xit")
        while choose != 'E':
            keyQueue = DSAQueue()
            valueQueue = DSAQueue()
            if choose.upper() == 'A':
                myTree.traverseInOrder(keyQueue, valueQueue)
                while(keyQueue.isEmpty() != True):
                    myKey = keyQueue.dequeue()
                    myValue = valueQueue.dequeue()
                    print(myKey, "->", myValue)
            if choose.upper() == 'B':
                myTree.traversePreOrder(keyQueue, valueQueue)
                while(keyQueue.isEmpty() != True):
                    myKey = keyQueue.dequeue()
                    myValue = valueQueue.dequeue()
                    print(myKey, "->", myValue)
            if choose.upper() == 'C':
                myTree.traversePostOrder(keyQueue, valueQueue)
                while(keyQueue.isEmpty() != True):
                    myKey = keyQueue.dequeue()
                    myValue = valueQueue.dequeue()
                    print(myKey, "->", myValue)
            choose = input("\nWhich serialisation file shall we read? Select either (A)InOrder, (B)PreOrder,(C) PostOrder, (E)xit")
    
    selection = input("What would you like to do? (1) Write a CSV file, (2) Write serialised file,(3) Read CSV, (4) Read serialised file,(5) Display tree,(6) Exit")
