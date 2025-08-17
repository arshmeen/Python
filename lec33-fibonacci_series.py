# The Fibonacci sequence is a series of numbers
# where each number is the sum of the two
# preceding numbers, starting with 0 and 1
# (or 1 and 1).
# This means the sequence begins
# 0, 1, 1, 2, 3, 5, 8, 13, and so on.

def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c

            print(c)

fib(5)