def merge(left, right, array):
    nl = len(left)
    nr = len(right)
    # i = j = k = 0
    i, j, k = 0,0, 0
    while i < nl and j < nr:
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < nl:
        array[k] = left[i]
        i += 1
        k += 1

    while j < nr:
        array[k] = right[j]
        j += 1
        k += 1


def mergeSort(array):
    n = len(array)
    if n < 2:
        return
    mid = n//2
    left = array[:mid]
    right = array[mid:]
    mergeSort(left)
    mergeSort(right)
    return merge(left, right, array)


# a = [1, 3, 4, 6, 0, 8, 7, 4, 4, 5, 6,7]
a = [1,5,7,8,3,4,6,8,9,4,2,21,4,4,6,7,8,9,9,7,6,4,3,2,2,45,6,8,9,1000]
# selectionSort(a)
mergeSort(a)
print(a)
