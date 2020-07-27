# ArrayJoin
"""
Joining means putting contents of two or more arrays in a single array.

In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.

We pass a sequence of arrays that we want to join to the concatenate() function,

along with the axis. If axis is not explicitly passed, it is taken as 0.
"""

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)


# SPlit

# Splitting NumPy Arrays
# Splitting is reverse operation of Joining.

# Joining merges multiple arrays into one
# and Splitting breaks one array into multiple.

# We use array_split() for splitting arrays,
# we pass it the array we want to split and the number of splits.

# Example
# Split the array in 3 parts:

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
