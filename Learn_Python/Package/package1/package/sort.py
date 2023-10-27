def selectionSort(list):
    """ sort by selection"""
    for i in range(len(list)): 
        min_idx = i 
        for j in range(i+1, len(list)): 
            if list[min_idx] > list[j]: 
                # check if left number is greater than right
                min_idx = j    
        # swap numbers    
        list[i], list[min_idx] = list[min_idx], list[i] 
    return list

def bubbleSort(list): 
    n = len(list) 
    for i in range(n): 
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            # traverse the listay from 0 to n-i-1 
            # Swap if the left number is greater than the right element 
            if list[j] > list[j+1] : 
                list[j], list[j+1] = list[j+1], list[j]
    return list

def insertionSort(list): 
    for i in range(1, len(list)): 
        key = list[i] 
  
        # Move elements of list[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < list[j] : 
                list[j + 1] = list[j] 
                j -= 1
        list[j + 1] = key
    return list

def mergeSort(list):
    if len(list) > 1:
        mid = len(list)//2 # Finding the mid of the listay
        L = list[:mid] # Dividing the listay elements
        R = list[mid:] # into 2 halves
        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half
 
        i = j = k = 0
        # Copy data to temp listays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1
    return list

def quickSort(list,low,high):
    if low < high: 
        # pi is partitioning index, list[p] is now 
        # at right place 
        pi = partition(list,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(list, low, pi-1) 
        quickSort(list, pi+1, high)
    return list

def partition(list,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = list[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   list[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            list[i],list[j] = list[j],list[i] 
  
    list[i+1],list[high] = list[high],list[i+1] 
    return ( i+1 )

def heapSort(list):
    n = len(list)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(list, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        list[i], list[0] = list[0], list[i]  # swap
        heapify(list, i, 0)
    return list

def heapify(list, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and list[largest] < list[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and list[largest] < list[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        list[i], list[largest] = list[largest], list[i]  # swap
 
        # Heapify the root.
        heapify(list, n, largest)

def radixSort(list): 
    # Find the maximum number to know number of digits 
    max1 = max(list) 
  
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1 / exp > 0: 
        countingSort(list, exp) 
        exp *= 10
    return list

def countingSort(list, exp1): 
  
    n = len(list) 
  
    # The output listay elements that will have sorted list 
    output = [0] * (n) 
  
    # initialize count listay as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (list[i] / exp1) 
        count[int(index % 10)] += 1
  
    # Change count[i] so that count[i] now contains actual 
    # position of this digit in output listay 
    for i in range(1, 10): 
        count[i] += count[i - 1] 
  
    # Build the output listay 
    i = n - 1
    while i >= 0: 
        index = (list[i] / exp1) 
        output[count[int(index % 10)] - 1] = list[i] 
        count[int(index % 10)] -= 1
        i -= 1
  
    # Copying the output listay to list[], 
    # so that list now contains sorted numbers 
    i = 0
    for i in range(0, len(list)): 
        list[i] = output[i] 