from array import *
array1 = array('i', [10,20,30,40,50])
print (array1[0])
print (array1[2])

for x in array1:
    print(x)
array1.insert(1,60)
print (array1)
array1.remove(40)
print (array1)