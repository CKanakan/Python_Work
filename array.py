"""import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)
"""
"""
import numpy as np

arr = np.array([1,2,3,4,5])

print(arr)
"""

import numpy as np

arr = np.array([1,2,3,4,5])

print(arr)

print(type(arr))


#2d array
#An array that has 1-D arrays as its elements is called a 2-D array.

#These are often used to represent matrix or 2nd order tensors.

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)



#3-D arrays
#An array that has 2-D arrays (matrices) as its elements is called 3-D array.

#These are often used to represent a 3rd order tensor.

#Example
#Create a 3-D array with two 2-D arrays,
#both containing two arrays with the values 1,2,3 and 4,5,6:

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

#Check Number of Dimensions?
#NumPy Arrays provides the ndim attribute
#that returns an integer that tells us how many dimensions the array have.

#Example
#Check how many dimensions the arrays have:

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)




# Higher Dimensional Arrays
# An array can have any number of dimensions.

# When the array is created, you can define the number of dimensions by using the ndmin argument.

# Example
# Create an array with 5 dimensions and verify that it has 5 dimensions:

#import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
