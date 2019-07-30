def binarySearch(a, x):
    start = 0
    end = len(a)-1
    return _binarySearch(a, start, end, x)

def _binarySearch(a, start, end, x):
    mid = (start + (end - start) // 2)
    if start > end:
        return False
    else:
        if x == a[mid]:
            return True
        elif x < a[mid]:
            return _binarySearch(a, start, mid-1, x)
        elif x > a[mid]:
            return _binarySearch(a, mid+1, end, x)
        else:
            return False

a = [1,2,3,4,5,6,7,8,9,10]
# print(binarySearch(a, 10))
x = binarySearch(a, 5)
print(x)
