# in the below case what will happen is we do
# know one argument for sure and we are not sure
# about the other arguments
# we can use variable length parameter

def person(name, *data):
    print(name)
    # this will be printed as tuple
    print(data)

person('navin',28,'Mumbai',1234567890)

# if we want to specify the type of other data we
# have if we use keyword argument it will throw
# an error at variable length parameter

# def person2(name, *data):
#     print(name)
#     # this will be printed as tuple
#     print(data)
#
# person('navin',age=28,city ='Mumbai',contact = 1234567890)

# to resolve this issue what we can do is

def person2(name, **data):
    print(name)
    # this will be printed as tuple
    print(data)

person2('navin',age=28,city ='Mumbai',contact = 1234567890)


# we can use the for loop to print key value pair, of data

def person3(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

person3('navin',age=28,city ='Mumbai',contact = 1234567890)