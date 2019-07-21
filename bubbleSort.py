#:: Bubble sort with a time complexity of O(n2)
def bubbleSort(array):
    isSwapped = False  #for efficiency or improved algorithm the flag stops code from running after all elements are sorted
    for k in range(0, len(array)-1):  #loop for determining the number of iterations
        for i in range(0, len(array)-k-1): #main loop for comparison.
        # len(array)-k-1 is used because at the end of each iteration part of the array is sorted
            if array[i] > array[i+1]:
                #:: Swap
                array[i], array[i+1] = array[i+1], array[i]
                Issorted = True
        if Issorted == False:
            break

a = [1, 3, 4, 6, 0, 8, 7, 4, 4, 5, 6,7]
# selectionSort(a)
bubbleSort(a)
print(a)
