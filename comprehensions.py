# Comprehensions
# comprehensions is a one line iteration of a collection

# the element on the left hand side is the element that will be added into the list
# the rest of the for loop proceeds as mostly normal
# by default x starts at 0
x = [x for x in range(5)]

# prints [0, 1, 2, 3, 4]
print(x)

# you can start your variable at a different number by simply adding it at the beginning
x = [x + 5 for x in range(5)]

# prints [5, 6, 7, 8, 9]
print(x)

# you can also create a list of all one number 
x = [0 for x in range(5)]

# prints [0, 0, 0, 0, 0]
print(x)

# you can also have comprehensions within comprehensions
x = [[0 for x in range(5)] for x in range(100)]

# prints [0, 0, 0, 0, 0] x 100
print(x)

# you can also use comprehension for incrementation 
# NOTE: this also shows a good use of the modulo operator
x = [i for i in range(105) if i % 5 == 0]

# prints [0, 5, 10,..., 95, 100]
print(x)

# you can do the same through dictionaries and other collections as well
x = {i:0 for i in range(105) if i % 5 == 0}

# prints the same list except the keys are all initialized at zero
print(x)

# sets
x = {i for i in range(105) if i % 5 == 0}

# prints {0, 5, 10,..., 95, 100} just possibly not in order
print(x)

# tuples
# NOTE: you must specifically type 'tuple' otherwise a generated object is returned
# this uses the tuple constructor
x = tuple(i for i in range(105) if i % 5 == 0)

# prints (0, 5, 10,..., 95, 100)
print(x)