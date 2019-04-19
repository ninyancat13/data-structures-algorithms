from hashTable import *

h = DSAHashTable()

print("-----Let us put in the values into the hashtable...----")
h.put("test" + str(0) ,0)
h.put("test" + str(2) ,2)
h.put("test" + str(4) ,4)
h.put("test" + str(6) ,6)
h.put("test" + str(20) ,20)


print("\n\n-------Display the hashtable-------")
h.display()
print("\n\n")

print("----Let us put in the values into the hashtable...----")
h.put("test" + str(40) ,40)
h.put("test" + str(60) ,60)
h.put("test" + str(60) ,60)
h.put("test" + str(80) ,80)
h.put("test" + str(88) ,88)

print("\n\n--------Display the hashtable---------")
h.display()
print("\n\n")

print("-----Let us put in the values into the hashtable...-----")
h.put("test" + str(400) ,400)
h.put("test" + str(600) ,600)
h.put("test" + str(600) ,600)
h.put("test" + str(800) ,800)
h.put("test" + str(808) ,808)

print("\n\n--------Display the hashtable--------")
h.display()


#Try to remove...
h.remove("test" + str(400))
print("\n\n")
h.display()



print("\n\n----------RandomNamesHashTable----------")

readfile = open('RandomNames7000(1).csv')
lines = readfile.readlines()
for i in range(len(lines)):
    key = lines[i].split(",")[0]
    value = lines[i].split(",")[1].strip()
    h.put(key, value)

h.display()
h.save()
