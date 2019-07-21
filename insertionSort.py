#:: Insertion sort with a complexity of O(n2)
#:: basically you are partioning the array into a sorted and unsorted part
def insertionSort(array):
    for i in range(1, len(array)):
        value = array[i]
        hole = i
        while hole > 0 and array[hole-1] > value:
            array[hole] = array[hole-1]
            hole = hole-1
        array[hole] = value


a = [1, 3, 4, 6, 0, 8, 7, 4, 4, 5, 6,7]
# selectionSort(a)
insertionSort(a)
print(a)
