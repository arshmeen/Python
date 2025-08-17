# filter is an inbuilt python function
# that takes up functions and gives the desired result
# after filtering the data as required


# it is a customized function for the use of
# filter function

print("Filter Function")
def is_even(n):
    return n%2 == 0

nums = [3,2,6,8,5,6,2,9]

# filter takes two arguments
# 1. function it is the logic of operation that we want
# 2. list of sequence

evens = list(filter(is_even, nums))

print(evens)

# instead we can use lambda function as well

even = list(filter(lambda x : x%2 == 0, nums))
print(even)

print("-----------------------------------")
print("Map Function")
# map function
# in bunch if values we can apply some operations
# or finding something

# map takes two arguments
# 1.function
# 2. list /iterable

# adding 2 to every value in the list
add_two = list(map(lambda n : n+2,nums))
print(add_two)

# multiplying 2

double = list(map(lambda x : x*2,nums))
print(double)

print("-----------------------------------")
print("Reduce Function")
# reduce is the part of functools module , we have to import it from there
# reduce take two arguments
# 1. function
# 2. iterable
from functools import reduce

sum = reduce(lambda a,b: a+b, nums)
print(sum)
print("-----------------------------------")