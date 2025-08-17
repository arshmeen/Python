def fact(x):
    fac = 1
    for i in range(1,x+1):
        fac = fac*i
    return fac

x = 5
n = fact(x)
print(n)