#ArrayIndexing

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])

#accesing elements from 2D array

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])


print('2nd element on 1st dim: ', arr[0, 1])
print('2nd element on 2st dim: ', arr[1, 1])

#Access the third element of the second array of the first array:

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])


#arr[0, 1, 2] prints the value 6.

#And this is why:

#The first number represents the first dimension, which contains two arrays:
#[[1, 2, 3], [4, 5, 6]]
#and:
#[[7, 8, 9], [10, 11, 12]]
#Since we selected 0, we are left with the first array:
#[[1, 2, 3], [4, 5, 6]]

#The second number represents the second dimension, which also contains two arrays:
#[1, 2, 3]
#and:
#[4, 5, 6]
#Since we selected 1, we are left with the second array:
#[4, 5, 6]

#The third number represents the third dimension, which contains three values:
#4
#5
#6
#Since we selected 2, we end up with the third value:
#6

#Negative Indexing
#Use negative indexing to access an array from the end.

#Example
#Print the last element from the 2nd dim:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])

#Slice elements from index 1 to index 5 from the following array:


arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])


#Use the minus operator to refer to an index from the end:

#Example
#Slice from the index 3 from the end to index 1 from the end:

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])


#Use the step value to determine the step of the slicing:

# Example
# Return every other element from index 1 to index 5:

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])
