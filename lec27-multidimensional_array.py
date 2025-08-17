from numpy import*

# 2-D array
arr1 = array([
    [1,2,3],
    [4,5,6]
])

print("2-D Array")
print(arr1)

# Applying different functions

# d.type to find the data type of the matrix
print("Applying Functions")
print("Type of the Matrix")
print(arr1.dtype)

# ndim function tells the number of dimensions does the matrix
# or the multi-dimensional array have
print("Number of Dimensions")
print(arr1.ndim)

# shape function
# it tells number of roes and columns does the matrix have
# rows x columns
# r,c

print("Shape")
print(arr1.shape)

# size function
# it tells the number of elements in the array
print("Size")
print(arr1.size)

# flatten function
# it is used to convert 2-D array into 1-D array

print("Flatten Function")
arr2 = arr1.flatten()
print(arr2)

# reshape function to covert 1D to 2D array
# we need to specify the number of rows and columns
print("Reshape")

arr3 = arr2.reshape(2,3)
print(arr3)

# matrix operationa

arr = array([
    [1,2,3,6],
    [4,5,6,7]
])

m = matrix(arr)

print(m)

# in matrix method we can use ; to differentaite
# between rows

m1 = matrix('11,2,3;4,5,6')
print(m1)

# diagonal elements
print(diagonal(m1))

# max value
print(m.max())

# adding two matrix
print(m+m1)

# multiplying
print(m*m1)