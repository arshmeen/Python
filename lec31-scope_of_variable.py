# global variable
a = 10

def something():
    # local variable
    a = 15
    print(a)

print(a)
something()

# preference is always given to local variable

# to use global variable we need to specify
# global variable_name

# var = globals() it gibes the access of all the global variable