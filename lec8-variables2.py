num = 5

# let's say we want its address
# we can use function known as id
# id(variable)

print(id(num))

a = 10
b = a
# in this case since the value of both the variables
# is same they both are going to have sa,e address
# this happens in python
print(id(a))
print(id(b))

# using type function we can get to know the
# typeof a variable

print(type(a))