from DSAHeap import *

heap = DSAHeap()

print("Let us add...")

heap.add(10)
heap.add(8)
heap.add(6)
heap.add(12)
heap.add(20)
heap.add(0)
heap.add(2)
heap.add(322)

print("\nWhat is the size of the heap?  ")
heap.size()

print("\nMax-sorted heap...")
heap.heapSort()


print("Now let us try the remove function")
heap.add(10)
heap.add(8)
heap.add(6)
heap.add(12)
heap.add(20)
heap.add(0)
heap.add(2)
heap.add(322)

print("What is the size now?")
heap.size()

print("Let us remove...")
heap.remove()
print("Done")

print("\nWhat is the size of the heap?  ")
heap.size()

print("\nMax-sorted heap...")
heap.heapSort()





print("\n\n\n\nNow let us sort out the RandomNames data...")
heap2 = DSAHeap()

fileobj = open("randomnames.csv")
lines = fileobj.readlines()

for line in lines:
    linesplit = line.split(",")
    heap2.add(linesplit[0])

heap2.heapSort()

#text_file = open("Output.txt", "w")
#text_file.write(heap2_output)
#text_file.close()

