# function for division

def div(a,b):
    print(a/b)

div(2,4)

# but what if we want to divide the bigger number with
# the smaller number everytime, we need to swap
# numbers so that numerator is greater than denominator

def div1(a,b):
    if a<b:
        a,b = b,a
    print(a/b)

div1(2,4)

# what if we don't want to change the function
# or maybe th efunction is in some other file
# then we can use decorators

# decorators - using decorators we can add extra
# features in the existing functions

# the below function will take div function
# as the parameter
def smart_div(func):
    # this inner function takes the same parameter
    # as the function div
    def inner(a,b):
        if a<b:
            a,b = b,a
        # we return the function we took as parameter
        # we want the changes in
        return func(a,b)
    return inner

div = smart_div(div)
div(2,4)