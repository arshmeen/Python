# two steps for creating a function
# 1. define it
# 2. call it

# syntax

# def func_name():
# these round brackets give away that this is a
# function not a variable
# a function can have multiple statements

# example 1

# defining a function
def greet():
    print("Hello")
    print("Good Morning")

# calling a function
# we have to call it explicitly
greet()

# function is a major helper we can assign
# various roles to this function

# using function helps in reusing the code

# example 2

# parameters/ arguments
def addition(a,b):
    print(a+b)


addition(3,4)

# there are two types of function
# printing values
# returning value

# returning value

def add(a,b):
    c = a+b
    return c

result = add(3,4)


def add_sub(a,b):
    c = a+b
    d = a-b
    return c,d

# when we are returning two values, we have to
# accept two values

res1, res2 = add_sub(3,4)

print(res1,res2)
