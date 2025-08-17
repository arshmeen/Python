# in case of for while loops is fir certain iterations
# where we specify conditions
# it is not the case in for loop, it works with sequence, list, tuple set, string

x = ['Damon', 25, 27.8]

# here "i" represents each element in the list at a time
# there is no need for condition and increment/decrement to be added

for i in x:
    print(i)

# range is used to write a sequence like 1-10
# the value is excluded , for example the 10 in the
# range () is excluded
for i in range(10):
    print(i, end = " ")

# we can also have a start point
print()
# last one will tell the difference between the next iteration
for i in range( 1, 21, 1):
    print(i, end = " ")

print()

for i in range( 1, 21, 2):
    print(i, end = " ")

print()

for i in range( 20, 0, -1):
    print(i, end = " ")

print()

for i in range(1,41):
    if i%5 == 0:
        print(i, end = " ")