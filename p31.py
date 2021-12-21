from numpy import *

arr1 = array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
    ])

m = matrix(arr1)
m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('2 2 2; 3 3 3; 4 4 4')

m3 = m1 * m2

print(m1)
print(m2)
print(m3)

#print(diagonal(m1))

#arr2 = arr1.flatten()

#arr3 = arr2.reshape(3, 2, 2)
#print(arr2)
#print(arr3)