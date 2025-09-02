import numpy as np

L = [9,6,2,8,1,0,4,7]
#creating array from list
ar = np.array(L)
print(ar)

ar = np.arange(6)# 0 to 5
print(ar)
ar = np.arange(6,10)#6 to 9
print(ar)
ar = np.arange(6,60,7)# 6 to 59 at the interval of 7 
print(ar)

ar = np.linspace(3,33,7)#interval = (33-3)/(7-1)  = 30/6 = 5 , 3,8,13,18,23,28,33   
print(ar)

#1. Create an array from a python list
ar = np.array([1,2,3,4,5])
print(ar)

#2. Create an array of zeroes
ar = np.zeros((2,3))
print(ar)

#3. Create an array of ones
ar = np.ones((3,2))
print(ar)

#4. Create an array filled with a specific value
ar = np.full((2,2), 7)
print(ar)

#5. Create an identity Matrix
ar = np.eye(4)# 4x4 identity matrix
"""
1000
0100
0010
0001
"""
print(ar)
#6. Create an array with a list of values
ar = np.arange(0, 10, 2)#Values from 0 to 8 with a interval count of 2, 2, 4, 6, 8, .
print(ar)
#7. Create an array with evenly spaced values
ar = np.linspace(0, 1, 5)#5 values from 0 to 1, d= (1-0)/(5-1) = 1/4 = 0.25, = 0, 0.25, 0.5, etc
print(ar)

#8. create an empty array(uninitialized values)
ar = np.empty(2)#May contain arbitary values
print(ar)

#arrange the elements in ascending order
print(np.sort(ar))
