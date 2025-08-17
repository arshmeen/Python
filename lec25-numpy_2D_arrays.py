# There are multiple ways to create arrays in python
# 1. array()
# 2. linspace()
# 3. logspace()
# 4. arange()
# 5. zeros()
# 6. ones()

from numpy import *
# using array method to create array
print("Array Method")

# specifying the type is not important here
arr = array([1,2,3,4,5])

# checking the data type of this array

print(arr.dtype)

# if we have any if those elements as floats
# instead of throwing an error it will change the
# data type of the whole array to float

arr2 = array([1,2,3,4,5.0])

print(arr2.dtype)

# if we want all the data types of a specific type we can
# mention that ,and it will get converted automatically

arr3 = array([1,2,3,4,5.0], int)

print(arr3)

arr4 = array([1,2,3,4,5.0], float)

print(arr4)

print("-----------------------------------")
print("Linspace Method")

# using linspace to create an error, it is a function from numpy itself
# it takes 3 parameters
# 1 - start
# 2 - stop
# 3 step - this will convert the values into number of parts in this
# in linspace the difference between the elements is always the same
# when the parts are created
arr5 = linspace(0,16, 20)

print(arr5)

# if in case you don't mention the number of steps
# the range will be divided into 50 parts by default

arr6 = linspace(0,20)
print(arr6)

print("-----------------------------------")
print("Arange Method")

# using arange() to create an array
# it takes 3 parameters
# 1 - start
# 2 - stop
# 3 step - this is difference between the two elements

arr7 = arange(0,15,2)
print(arr7)

# using logspace method
# it takes 3 parameters
# 1 - start
# 2 - stop
# 3 step - this will convert the values into number of parts in this
# so in this case the difference between the elements is nit the same
# it is based on the log
# log 10 (start) to log 10 stop , in steps number of parts

print("-----------------------------------")
print("Logspace Method")

arr8 = logspace(1,40,5)
print(arr8)

print("-----------------------------------")
print("Zeros Method")

# it is used when we want an array of size n
# and we want all the elements if the array to be zero this array is used

arr9= zeros(5)
print(arr9)
# we want integer values

print("printing integer values")
arr9b = zeros(5,int)
print(arr9b)


print("-----------------------------------")
print("Ones Method")

# it is used when we want an array of size n
# and we want all the elements if the array to be one this array is used

arr10 = ones(5)
print(arr10)

print("printing integer values")
arr10b = ones(5,int)
print(arr10b)
