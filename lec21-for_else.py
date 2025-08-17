nums = [12,15,18,21,26]

# check if the above it has number divisible by 5
for num in nums:
    if num%5 == 0:
        print(num)

print()

# multiple we can use break

nums2 = [12,15,18,25,26]

# check if the above it has number divisible by 5
for num in nums2:
    if num%5 == 0:
        print(num)

print()

for num in nums2:
    if num%5 == 0:
        print(num)
        break

print()

# if there isn't any
nums2 = [12,14,18,24,26]
for num in nums2:
    print(num)

else:
    print("Not Found")
