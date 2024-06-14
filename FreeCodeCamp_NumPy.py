import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

print(np.__version__)

##Array filled with 0s


arr1 = np.array([0] *10)
print(arr1)


arr2 = np.arange(10,50) #Array with 10-50
print(arr2)

arr3 = np.ones([2,2], dtype = np.int64) #2x2 array with ones 
print(arr3)

arr4 = np.ones([3,2], dtype= np.float64)
print(arr4)

X = np.arange(4 , dtype=np.int64)

print(X)
arr5 = np.ones_like(X)
print(arr5)

Y = np.array([[1,2,3], [4,5,6]], dtype=np.int64)
print(np.zeros_like(Y))

mat1 = np.ones([4,4], dtype=np.int64) * 5 #Creating array of 4x4 and multiplying the numbers in that array by 5 
print(mat1)

T = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]], dtype=np.int64)
mat2 = np.ones_like(T) * 7
print(mat2)

print(np.identity(3))

##Array filled with 3 random int from 1-10

arr6 = np.random.randint(10, size= 3)
print(arr6)

arr7 = np.random.random((3,3,3)) ##random retruns floats when it is a variable 
arr8 = np.random.randn(3,3,3)#randn returns floats when it is a variable
print(arr7, arr8)


plist = [1,2,3,4,5]
arr9 = np.array(plist)
print(plist, type(plist),arr9, type(arr9)) ##Convert python list to numpy array

arr10 = np.array([1,2,3,4,5], dtype=np.int64)

arr11 = np.copy(arr10) #Copy array with different ID 

print(arr10, id(arr10), arr11, id(arr11)) 


arr12 = np.arange(1,11)
print(arr12)

arr13 = np.arange(1,11, 2, dtype=np.int64) ##Array 1-10 inputing every 2
print(arr13)

arr14 = np.arange(1,11, dtype=np.int64)[::-1] #[start:end:step (-) inverse order]
print (arr14)

arr15 = np.arange(9).reshape(3,3) #Making array 0-8 and reshaping it to a 3x3
print(arr15)



