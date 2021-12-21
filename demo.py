from array import *
vals = array('i', [3,9,-8,6,4,2])
newArr = array(vals.typecode, (a*a for a in vals))


i =0

while i < len(newArr):
    print(newArr[i])
    i+=1
