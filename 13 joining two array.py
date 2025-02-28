# import numpy as np
#
# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# arr = np.concatenate((arr1, arr2))
#
# print(arr)


import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)#we can use 0 and 1 to concatenate array

print(arr)
