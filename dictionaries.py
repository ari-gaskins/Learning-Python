# Dictionaries
# dictionaries are similar to hashtables or maps
# dictionaries include key: value pairs
# values are some valid data type
# this is what it looks like
x = {'key': 4}

# you can access values using the keys
# prints 4
print(x['key'])

# you can add a key to your dictionary by creating a new key and giving it a value
x['key2'] = 5

# keys do not need to be the same data types nor do they have to be only strings
x[2] = 8

# prints dictionary
print(x)

# you can also set values as a list
x['key4'] = [1, 2, 3, 4]

print(x)

# we can check if something is in the dictionary 
# NOTE: this returns true, not the value
print('key' in x)

# you can get all the values from the dictionary as well 
# NOTE: this returns the values but it also says 'dict_values'
print(x.values())

# if you want the values by themselves printed try this
print(list(x.values()))

# you can also print keys the same way
print(list(x.keys()))

# you can delete a key and its value like this
del x['key4']

print(x)

# if you'd like to iterate over every key and value
for key, value in x.items():
    # essentially another way to print the dictionary
    print(key, value)
# OR
for key in x:
    print(key, x[key])

# if you want to access a value given a key, use the get() method 
# prints 5
print(x.get('key2'))