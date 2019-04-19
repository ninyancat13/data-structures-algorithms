# hanoi.py - Towers of Hanoi

def hanoi(n):
    hanoiR(n, 1, 3)

def hanoiR(n, source, dest):
    if (n==1):
        print('moveDisk(', source, ',', dest, ')')
    else:
        tmp = 6 - source - dest
        print('hanoi(', n-1, ',', source, ',', dest, ')')
        hanoiR(n-1, source, dest)
        print('moveDisk(', source, ',', dest, ')')
        print('hanoi(', n-1, ',', tmp, ',', dest, ')')
        hanoiR(n-1, tmp, dest)

numDisk = int(input("Enter Number of Disk"))
hanoi(numDisk)
