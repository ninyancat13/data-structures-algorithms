from collections import deque

s = deque()

s.append(1)
s.append(2)
s.append(3)
s.append(4)

print(s)
if len(s) == 4:
    print("Test passed getCount")
else:
    print("Test failed getCount")

print(s.popleft())
print(s.popleft())
print(s.popleft())
print(s.popleft())

try:
    print(s.popleft())
except:
    print("Test passed QueueUnderflowError")
else:
    print("Test failed QueueUnderflowError")


s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
