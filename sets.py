# Sets
# a set is a data type
# defined as an unordered unique collection of elements, 
# no duplicate elements and order or frequency is not kept track of
# sets are extremely when trying to perform remove(), add(), or simply check if element is present
# use sets if you only care about whether or not something exists not frequency or order

# this should be used if an empty set is being created
x = set()

# this can be used only if you intend to place elements in your set
# because if you don't place elements you will accidentally create a dictionary
s = {4, 32, 2, 2}

# prints {32, 4, 2} because no duplicates and no order
print(s)

# you can add elements like this
# the argument is the element you wish to add and it won't add anything if its already there
s.add(5)

# prints {4, 5, 2, 32}
print(s)

# you can also remove elements like this 
# the argument is the element you wish to remove
s.remove(2)

# prints {32, 5, 4}
print(s)

# you can check if element is present by seeing if 'in' statement is true
print(4 in s)

# you can also combine sets
s2 = {2, 4, 87, 9}

# using the union() function with argument of what set you want to combine with looks like this
print(s.union(s2))


# you can also find the difference between two sets
print(s.difference(s2))

# you can also find the intersection between two sets
print(s.intersection(s2))
