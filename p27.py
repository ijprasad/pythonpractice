from array import *

arr = array('i', [])

n = int(input("Enter length of the array"))

for i in range(n):
    x = int(input("Enter next value"))
    arr.append(x)

print(arr)

y = int(input("Enter value to search"))
for i in range(len(arr)):
    if arr[i] == y:
        print (i)
        break

else:
    print ("value not found")
