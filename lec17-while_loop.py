i = 1  # initializing the variable
while i<=5:  # condition to check
    # code to execute while condition is true
    print(i)
    i += 1 # incrementing the variable to avoid infinite loop

# while loop example
# printing numbers from 1 to 5  
# debugging the code

# using decrement
i = 5  # initializing the variable
while i >= 1:  # condition to check
    # code to execute while condition is true
    print(i)
    i -= 1  # decrementing the variable to avoid infinite loop

# loop nesting
# nested while loop example
i = 1  # outer loop variable
while i <= 3:  # outer loop condition
    j = 1  # inner loop variable
    while j <= 2:  # inner loop condition
        print("i =", i, ", j =", j)  # code to execute in inner loop
        j += 1  # incrementing inner loop variable
    i += 1  # incrementing outer loop variable

# end = "" to avoid newline after each print
i = 1  # initializing the variable
while i <= 5:  # condition to check
    print(i, end=" ")  # code to execute while condition is true
    i += 1  # incrementing the variable to avoid infinite loop


# code to practice
# Write a code to print all the values from 1 to 100. Skip the numbers which are divisible by 3 or 5.

print("Numbers from 1 to 100, skipping those divisible by 3 or 5:")

i = 1

while i<=100:
    if i % 3 == 0 or i % 5 == 0:
        i += 1  # skip the number
        continue  # continue to the next iteration
    print(i)  # print the number if not skipped
    i += 1  # increment the variable


# 2) Write a code to print below pattern.
# pattern:
# ####
# ####
# ####
# ####

print("Pattern of hashes:")

i = 1  # initializing the variable
while i <= 4:  # condition to check for 4 rows
    j = 1  # inner loop variable for columns
    while j <= 4:  # condition to check for 4 columns
        print("#", end="")  # print hash without newline
        j += 1  # increment inner loop variable
    i += 1  # increment outer loop variable