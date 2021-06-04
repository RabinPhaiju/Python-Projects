# from package.calc import adder,subtractor
# from package.calc import *
# from package calls __init__

# help(adder) # documentation
# print(adder(2,4))
# print(subtractor(2,4))

from package import *

list = [29,50,44,36,23,67,46,87,34]
print(selectionSort(list))
print(bubbleSort(list))
print(insertionSort(list))
print(mergeSort(list))
print(quickSort(list,0,len(list)-1))
print(heapSort(list))
print(radixSort(list))

