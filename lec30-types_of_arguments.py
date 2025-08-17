# addition of two numbers
# if we are accepting the arguments
# we have to oass the arguments as well

def add(x,y):
    c= x+y
    print(c)

add(5,6) # these 5,6 are arguments

# there are two types of arguments
# 1. Actual Arguments
# it is of 4 types

# a. Position

# A positional argument is an argument passed
# to a function in the correct order,
# where the position determines which parameter
# it’s assigned to
def person(name,age):
    print(name)
    print(age)

person("arshi",25)

# b. Keyword
# if we don't know the position of arguments
# we can write the name of the argument to specify
# example

person(name = 'nikhil', age=28)

def person2(name,age = 25):
    print(name)
    print(age)

# default arguments
# A default argument is a function parameter
# that has a predefined value, which is used
# if no value is provided for that parameter
# when calling the function

person2("arshi")
# if we give it then it will override
person2('nikhil',28)


# d. Variable Length

# A variable-length argument allows a function
# to accept any number of arguments,
# using *args for positional arguments or
# **kwargs for keyword arguments

# this star means multiple values can be added
def add2(*y):
    c= 0

    for i in y:
        y = y+ 1

add2(1,2,3,4)


# 2. Formal Arguments

# Formal arguments are the variables defined in
# a function's definition that receive values
# from the arguments passed during the function
# call
# They act as placeholders for the actual data
# the function will work with

# Example:

def greet(name, message):  # name and message are formal arguments
    print(f"Hello {name}, {message}")

greet("Arshi", "Welcome!")
# "Arshi" and "Welcome!" are actual arguments

# Here:

# Formal arguments:
# name, message (defined in the function header)

# Actual arguments:
# "Arshi", "Welcome!" (passed during the call)