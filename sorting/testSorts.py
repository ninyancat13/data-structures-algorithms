from DSAsorts import *

array = [1,3,5,13,2,40,29,17,20,21]
array1 = [1,3,5,13,2,40,29,17,20,21]
array2 = [1,3,5,13,2,40,29,17,20,21]
array3 = [1,3,5,13,2,40,29,17,20,21]
array4 = [1,3,5,13,2,40,29,17,20,21]

print("This is the original array:" , array)
print("This is the sorted array using bubble:\n")
bubbleSort(array)
print(array)

print("This is the original array:" , array1)
print("This is the sorted array using insertion:\n")
insertionSort(array1)
print(array1)

print("This is the original array:" , array2)
print("This is the sorted array using selection:\n")
selectionSort(array2)
print(array2)

print("This is the original array:" , array3)
print("This is the sorted array using merge sort:\n")
mergeSort(array3)
print(array3)

print("This is the original array:" , array4)
print("This is the sorted array using quick sort:\n")
quickSort(array4)
print(array4)
