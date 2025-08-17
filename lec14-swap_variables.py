# swapping variables
a = 5
b = 10

# using a temporary variable
# to hold the value of one variable while swapping
# swap
temp = a
a = b
b = temp

print(a)
print(b)

# without using a temporary variable
# using arithmetic operations
a = a + b
b = a - b
a = a - b

print(a)
print(b)

# using XOR operation
a = 5
b = 10

a = a ^ b
b = a ^ b
a = a ^ b

print(a)
print(b)

# another way tuple unpacking
# this is a pythonic way to swap variables

a, b = 5, 10
a, b = b, a