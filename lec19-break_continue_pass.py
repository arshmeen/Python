x = int(input("How may candies you want"))

i = 1

while i<=x:
    print("Candy")
    i+=1

print()

total = 15

# break
xn = int(input("How may candies you want"))
while i<=xn :
    if xn>total:
        print("Out of Stock")
        break
    print(i)

print("---------------------")

for i in range(1,101):
    if i % 3 == 0:
        continue
    print(i)

# pass

# don't print odd numbers
for i in range(1,101):
    if i % 2 == 1:
        pass
    else:
        print(i)