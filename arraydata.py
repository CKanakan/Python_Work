#array data

# Below is a list of all data types in NumPy
"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

#Get the data type of an array object:

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)


#For i, u, f, S and U we can define size as well.

#Example
#Create an array with data type 4 bytes integer:

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)


#Change data type from float to integer by using 'i' as parameter value:


arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)



# Copy
# Make a copy, change the original array, and display both arrays:

arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# View
# Make a view, change the original array, and display both arrays:

arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# Make a view, change the view, and display both arrays:

arr = np.array([1,2,3,4,5])
x = arr.view()
x[0] = 31

print(arr)
print(x)

# Print the value of the base attribute to check
#if an array own it's data or not

arr = np.array([1,2,3,4,5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)
