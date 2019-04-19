from stacks_queues import *
import numpy as np

stack = DSAStack()
print("empty?:", stack.isEmpty())
#stack.push(1)
#stack.push(1)
#stack.push(1)

#for x in range(100):
#    stack.pop()

for x in range(100):
    stack.push(1)

#for x in range(1):
#    stack.push(1)

print("Get count:", stack.getCount())
stack.display()
print("top value is", stack.top())
print("full?:", stack.isFull())

stack.pop()
stack.pop()
stack.pop()
stack.display()
print("Get count:", stack.getCount())
#print("top value is", stack.top())
print("empty?:", stack.isEmpty())
print("full?:", stack.isFull())

#remember to do exception handling to check if stackoverflow underflow works
#use nameerror

#try:
#    for x in range(101):
#        stack.push(1)
#except StackOverflowError:
#    print("Too many numbers added, stack is overflowing")
#
#
#try:
#    for x in range(50):
#        stack.push(1)
#except StackUnderflowError:
#    print("Too few numbers added, stack is underflowing")
#

queue = DSAQueue()
print("empty?:", queue.isEmpty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.display()

print("Get count:", queue.getCount())
print("empty?:", queue.isEmpty())
print("full?:", queue.isFull())

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.display()


