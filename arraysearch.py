#Array search, sort,

# Searching Arrays
# You can search an array for a certain value,
# and return the indexes that get a match.

# To search an array, use the where() method.

# Example
# Find the indexes where the value is 4:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)


# The example above will return a tuple: (array([3, 5, 6],)

# Which means that the value 4 is present at index 3, 5, and 6.

"""Example
Find the indexes where the values are even:

import numpy as np
"""


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)




# Search Sorted
# There is a method called searchsorted()
# which performs a binary search in the array,
# and returns the index where the specified
# value would be inserted to maintain the search order.

# The searchsorted() method is assumed to be used on sorted arrays.

# Example
# Find the indexes where the value 7 should be inserted:

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)



# Sorting

# Sorting Arrays
# Sorting means putting elements in a ordered sequence.

# Ordered sequence is any sequence that has an order corresponding to elements,
# like numeric or alphabetical, ascending or descending.

# The NumPy ndarray object has a function called sort(), that will sort a specified array.

# Example
# Sort the array:

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))



# Sort the array alphabetically:


arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))



"""Sorting a 2-D Array
If you use the sort() method on a 2-D array, both arrays will be sorted:

Example
Sort a 2-D array:

import numpy as np
"""

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))
