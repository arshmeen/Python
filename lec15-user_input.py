# taking user input
# input function returns a string
# we can convert it to int or float if needed
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello, " + name + "! You are " + age + " years old.")
# converting age to integer
age = int(age)  

# takinhg two numbers as input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# performing addition
sum_result = num1 + num2

print("The sum of", num1, "and", num2, "is:", sum_result)

# index value for the string enterted by the user for the character input needed
char_index = int(input("Enter the index of the character you want to access: "))
print(char_index[0])

# eval can not be used with input function
# eval is used to evaluate an expression
# it can be used to evaluate mathematical expressions
expression = input("Enter a mathematical expression (e.g., 2 + 3): ")
# using eval to evaluate the expression
result = eval(expression)
print("The result of the expression is:", result)

# using argv
import sys
# sys.argv is a list of command line arguments
# the first argument is the script name