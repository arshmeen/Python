
def count(lst):
    odd = 0
    even = 0

    for i in  lst:
        if i % 2 == 0:
            even += 1

        else:
            odd += 1

    return even, odd




lst = [10,23,45,67,89,54,67]

even, odd = count(lst)

print(even)
print(odd)