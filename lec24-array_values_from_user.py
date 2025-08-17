# the way to create an empty array
from array import*
arr = array('i',[])

# asking the length of the array
n = int(input("Enter the length of the array"))

for i in range(n):
    x = int(input("Enter the element"))
    # adding elements in the array
    arr.append(x)

print(arr)

# trying to find the index of the element by asking the
# user to tell which elements user wants to find

# method 1
# manually

val = int(input("Enter the value for search"))

# counter variable to find the index value
k = 0
for e in range(n):
    if e == val:
        print(k)
        break

    k += 1

# method 2
# function
print(arr.index(val))