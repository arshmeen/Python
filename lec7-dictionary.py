# key-value pair
# key is immutable

data = {
    1: "Arshi",
    2: "Anhad"
}

data2 = data.get(1)

print(data)
print(data2)

# if the key is not found
data3 = data.get(3, 'Not Found')
print(data3)  # index 3 was not there in the dict

# making dict using lists
keys = ['show1', 'show2', 'show3']
values = ["TVD", "ST", "MT"]

dict1 = dict(zip(keys, values))
print(dict1)

# how to add data
dict1['show4'] = ['DN']
print(dict1)

# deletion
del dict1['show3']
print(dict1)

# dict can be nested