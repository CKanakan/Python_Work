#Array shape/reshape

# Get the Shape of an Array
# NumPy arrays have an attribute called shape that returns a tuple with each
# index having the number of corresponding elements.

# Print the shape of a 2-D array:
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

# The example above returns (2, 4), which means that the array has 2 dimensions,
# and each dimension has 4 elements.

# Convert the following 1-D array with 12 elements into a 2-D array.

# The outermost dimension will have 4 arrays, each with 3 elements:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

# Convert the following 1-D array with 12 elements into a 3-D array.

# The outermost dimension will have 2 arrays that contains 3 arrays,
# each with 2 elements:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)

# Can We Reshape Into any Shape?
# Yes, as long as the elements required for reshaping are equal in both shapes.

# We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array
# but we cannot reshape it into a 3 elements 3 rows 2D array
# as that would require 3x3 = 9 elements.

# Unknown Dimension
# You are allowed to have one "unknown" dimension.

# Meaning that you do not have to specify an exact number for
# one of the dimensions in the reshape method.

# Pass -1 as the value, and NumPy will calculate this number for you.

# Example
# Convert 1D array with 8 elements to 3D array with 2x2 elements:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)


# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.

# We can use reshape(-1) to do this.

# Example
# Convert the array into a 1D array:

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)


# Iterating

# If we iterate on a 1-D array it will go through each element one by one.

# Example
# Iterate on the elements of the following 1-D array:

arr = np.array([1, 2, 3])

for x in arr:
  print(x)

# Iterate on the elements of the following 2-D array:

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)


# To return the actual values, the scalars,
# we have to iterate the arrays in each dimension.

# Example
# Iterate on each scalar element of the 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)


"""
Iterate on the elements of the following 3-D array:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

"""


# To return the actual values, the scalars,
# we have to iterate the arrays in each dimension.

# Example
# Iterate down to the scalars:

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)
