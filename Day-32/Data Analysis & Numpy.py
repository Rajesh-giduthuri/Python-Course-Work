#Data Analysis : collection,cleaning,processing 
#Numpy : Numarical Python (faster than normal list)

import numpy as np
arr=np.array([3,3,5,8,9])
print(arr)
print(arr.ndim)

arr1=np.array([[1,4,3],[5,3,8],[9,2,6]])
print(arr1)
print(arr1.ndim)

print(arr.shape)
print(arr1.shape)

print(arr.size)
print(arr1.size)

#array operations
n1=np.array([10,20,30])
n2=np.array([1,2,3])
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1//n2)

#scalar operation
print(n2+5)
print(n2-5)
print(n2*2)
print(n2//2) 

#aggregate functions
print(np.min(n1))
print(np.max(n1))
print(np.mean(n1))
print(np.sum(n1))
print(np.sqrt(n2))
print(np.pow(n2,2))

