# all the values of the same type
# they dont have any specfic size in python


from array import*


vals = array('i', [1,4,8,9])

print(vals)

# only one type of all variables


# it will give the size if the array

# other functions are there as well
print(vals.buffer_info())

for i in range(4):
    print(vals[i])

# other way

for e in vals:
    print(e)

# copying array, without knowing the type of array

# step 1 - getting the type
nArr = array(vals.typecode), (a*a for a in  vals)
