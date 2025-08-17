# everything in python is object
# there isn't any concept of pass by value
# and pass by reference
def update(x):
    x = 8
    print(x)

update(10)


def update2(x):
    x = 8
    print(x)
a = 10

update2(10)
print("a:",a)