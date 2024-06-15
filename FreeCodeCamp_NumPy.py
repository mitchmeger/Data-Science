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

#show memory 

arr16 = np.zeros([10,10])
print("%d bytes" % (arr16.size * arr16.itemsize)) #Getting memory of array 

###Array indexing 

arr17 = np.arange(10)
print(arr17)
print(arr17[0]) #First element 

print(arr17[-1]) #Last element

print(arr17[0:3]) #First 3 elements 

print(arr17[1:-1]) #Middle elements 

arr18 = arr17[:][::-1]
print(arr18) #Array in reverse order

print(arr17[::2]) #Elements in odd position

arr19 = np.arange(16).reshape(4,4)
print(arr19)

print(arr19[0])#First row 

print(arr19[-1]) #Last row

print(arr19[0][0]) #First element in first row

print(arr19[-1][-1])

print(arr19[1:-1, 1:-1]) ##Middle row elements 

print(arr19[0:2, 0:2])#Frist 2 rows first 2 elements 

print(arr19[2:, 2:]) #Last 2 two last 2 elements but this requires knowledge of shape of matrix and how many rows and columns lol

###Array manipulations 

arr20 = np.arange(20, dtype=np.int64)

arr21 = np.float64(arr20)
arr22 = np.array(arr21, np.float64) ##Changing int to float 

print(arr20, type(arr20), arr21, type(arr21), arr22, type(arr22)) 

print(arr21[::-1]) #Reversing order 

arr23 = [13,-5,-7,21,93,31,-9]
print(arr23)
arr24 = sorted(arr23) ##Sort array .sort() returned none for me for some reason
print(arr24)

#Chagne 5th element to 1


arr25 = [-1,4,5,13,-13, 21 ,-21]

arr26 = arr25[5] = 1 #Replacing 5th index to 1 
#print(arr25,arr26)

arr27 = np.zeros(10)

print(arr27)
arr27[5] = 1 # replacing 5th index with 1 
print(arr27)

arr28 = [10,20,30,40,50]
print(arr28)

arr28[-1] = 40
print(arr28)

arr29 = np.arange(16).reshape(4,4)
print(arr29)

arr29[-1] = 1 #Changing last row to all ones but can replace with a whole new array arr29 [-1] = np.array([1,1,1,1])
print(arr29)

arr29[-1][-1] = 0 ##Changing last row last element to zero but can replace it with array like in line 153 can also use [-1,-1] in array 

print(arr29)

arr30 = arr29 +5 
print( arr30)
##Boolean 
arr31 = np.array([-1,2,0,-4,5,6,0,0,-9,10])
mask = arr31<=0 #Masking all negative numebrs 
print(mask)

arr32 = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
mask = arr32<=0 #Lessthan and equal to 0
print(arr32[mask])##Creaing mask and returning all of the numbers with mask 'true' in the array 

mask = arr32>5 #Mask greater than 5 
print(arr32[mask])

mean = arr32.mean()
print(mean)
mask = arr32>mean
print(arr32[mask]) #mask = (arr32>arr32.mean()) Can also use this 

mask = (arr32 == 2) | (arr32 ==10) ##manually checking in the array wehre arr32 == 2 or ==10 dont forget () fucking moron
print(arr32[mask])

##Logic funtions 













