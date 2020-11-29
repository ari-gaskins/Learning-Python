# Map and Filter 
# these functions can make use of lambdas
x = [1, 2, 4, 5, 3, 3, 21, 2, 21, 2, 313, 1, 23, 142, 4]

# map() takes a function as an argument (and the second argument is the list being passed)
# and it is meant to map the list as a new list
# lambdas are useful here if you want a simple change done to the list
mp = map(lambda i: i + 2, x)

# NOTE: map() returns a map object so a list() function may be recommended, 
# though you can iterate over the object as well
print(list(mp))

# filter() also takes a function argument and a variable passed argument 
# the function is meant to check that the items in the list return true 
# those that return true can be added to the new list
# for example this lambda checks if the items are even
fil = filter(lambda i: i % 2 == 0, x) 

# NOTE: filter() returns a filter object so a list() function may be recommended, 
# though you can iterate over the object as well
print(list(fil))

# you can also of course pass a regular function through these functions, 
# but a lambda can be a lot easier