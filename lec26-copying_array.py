from numpy import*

# adding specific value to all the elements of an array

print("Adding specific number to all the elements if the array")
arr = array([1,2,3,4,5])
print(arr)
# adding 5 in each of the elements of the array

# method 1
# manually
for i in range(5):
    arr[i] = arr[i] + 5

print("printing array after addition")
print(arr)

# method 2

arr = arr + 5

print("addition using array function")
print(arr)

print("-----------------------------")
print("Adding two arrays")

# adding two arrays
# manually

print("Manually")

arr1 = array([1,2,3,4,5])
print(arr1.dtype)
arr2 = array([6,7,8,9,10])
print(arr2.dtype)
arr3 = zeros(5,int)
for i in range(5):
    arr3[i] = arr1[i] + arr2[i]

print(arr3)


# using array functions
# it is also called vectorized operation

print("array functions")
print("vectorized operation")

arr4 = array([1,2,3,4,5])
arr5 = array([6,7,8,9,10])

arr6 = arr4 + arr5

print(arr6)

print("-----------------------------")
print("Trigonometric values")
# we can also find trigonometric values of the array

print("Sine Values")
print(sin(arr))

print("Cosine Values")
print(cos(arr))

print("Tan values")
print(tan(arr))

print("-----------------------------")
print("Logarithmic values")

print(log(arr))

print("-----------------------------")
print("square roots")

# Printing the square root of the numbers
print("square root")

print(sqrt(arr))

print("-----------------------------")
print("Sum of array")

# sum of an array
# manual

print('manual')
sum_array = 0

for i in range(5):
    sum_array = sum_array + arr[i]

print(sum_array)

print("Sum using array functions")

array_sum = sum(arr)

print(array_sum)

print("-----------------------------")
print("Maximum value in array")


print("manual")
arr7 = array([34,87,91,57,84])
mx = -1

for i in range(5):
    if arr7[i] > mx:
        mx = arr7[i]

print(mx)

print("using array function")
mx_arr = max(arr7)

print(mx_arr)

print("-----------------------------")
print("Minimum value in array")

print("manual")

mn = arr7[0]

for val in arr7:
    if val < mn:
        mn = val

print(mn)

print("Array Function")
mn_arr = min(arr7)
print(mn_arr)


# sort array

arr_sort = zeros(5)
print(arr_sort)

print("-----------------------------")
print("Sorting in array")

# using the function sort we can sort the array in ascending or descending order
# sorting in ascending order

print("ascending order")
asc_sort = sorted(arr7)
print(asc_sort)

print("descending order")
des_sort = sorted(arr7, reverse=True)

print(des_sort)

print("-----------------------------")
print("Concatenate of two array")

# using concatenate function

arr_concat = concatenate([arr1,arr2])
print(arr_concat)

print("-----------------------------")
print("Copying Array")

print('Aliasing')
arr_copy = arr1

print("printing copied array")
print(arr_copy)

# printing the addresses of the arrays

print("addresses")
print(id(arr1))
print(id(arr_copy))

# They both have the same address
# so it means both point at the same array
# this is known as Aliasing

# if we want to have two different arrays
# with different addresses we can do that
# using view() function
print("using view function")
copy_arr = arr1.view()

print("addresses")
print(id(arr1))
print(id(copy_arr))

# but there is still one issue
# there are two types of the copies
# 1. shallow copy
# means even after having the different address the copies are still
# dependent on each other, any changes made to one
# would affect the other as well

print("shallow copy")

arr1[1] = 7
print("after changing one of the values of the original array")
print("original array")
print(arr1)

print("copied array")
print(copy_arr)

# 2.deep copy
# even after changing the value in the original array there won't
# be any changes in the copied array

cp_arr = arr2.copy()

print("shallow copy")

arr2[1] = 3
print("after changing one of the values of the original array")
print("original array")
print(arr2)

print("copied array")
print(cp_arr)