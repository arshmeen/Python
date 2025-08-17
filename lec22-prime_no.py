# way 1

num = int(input("Enter a number"))

for i in range(2,num):
     if num% i == 0:
         print("Non - Prime")
         break
else:
    print("Prime")

# way 2

num1 = int(input("Enter a number"))

for i in range(2,num1):
     if num1% i == 0:
         print("Non - Prime")
         break
else:
    print("Prime")

# way 3

import math

num2 = int(input("Enter a number"))

x = math.sqrt(num2/2) + 1

for i in range(2,x):
     if num2% i == 0:
         print("Non - Prime")
         break
else:
    print("Prime")