from numpy import *

arr = array([15, 12, 30, 14, 5])
#arr2 = array([16, 26, 36, 46, 56])

#arr = arr1 +arr2

arr1 = arr.copy()
#arr[1] = 122
arr.sort()

print(arr)
print(arr1)
print(id(arr))
print(id(arr1))