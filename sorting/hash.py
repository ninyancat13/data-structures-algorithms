h = {}

h[0] = "test 0"
h[1] = "test 1"
h[3] = "test 3"
h[4] = "test 4"
h[20] = "test 20"


print("\n\n")
print("Try to print dictionary...")
print(h)
print("\n\n")

h[30] = "test 30"
h[40] = "test 40"
h[50] = "test 50"
h[60] = "test 60"
h[70] = "test 70"

print("\n\n")
print(h)
print("\n\n")


h[400] = "test 400"
h[500] = "test 500"
h[600] = "test 600"
h[700] = "test 700"


print("\n\n")
print(h)

del h[60]
print("\n\n")
print(h)


#readfile = open("RandomNames7000.csv")
#lines = readfile.readlines()


#for i in range(len(lines)):
#    key = lines[i].split{",")[0]
#    value = lines[i].split(",")[1].strip()
#    h[key] = value

#print(h)
