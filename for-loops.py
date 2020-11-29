# for loops
# for loops allow you to iterate a loop a set number of times
# syntax is for variable in whateveryouwanttoiteratethrough(): 
# the range() function creates a collection based on the number in the argument(s)
# range() function can have up to three arguments: start, stop, step
# this is: number to start at, number to stop at, number to step at
# if there is only one argument in range then by default it is the stop argument
# by default start = 0, step = 1
# stop number always returns one less than what is written
# two arguments is by default start, stop
# start number is always included
for i in range(10):
# prints numbers 0 through 9
    print(i)

for i in range(10, -1, -1):
    # prints 10 to 0 
    print(i)

# if the start is already past the stop, nothing will happen
for i in range(-10, -1, -1):
    print(i)

# you can also loop through a list or tuple 
# like this
for i in [4, 5, 6]:
    # prints the list
    print(i)

for i in (4, 5, 6):
    # prints the tuple
    print(i)

# OR like this
x = [4, 5, 6]

# range() function works with len() function up to the length number because it won't be included in the indexes anyway
for i in range(len(x)):
    # using x and the square brackets allows the index to be i but the output to be the list or tuple
    # prints the list
    print(x[i])

x = (4, 5, 6)

for i in range(len(x)):
    # prints the tuple
    print(x[i])

# OR like this 
x = [4, 5, 6]


for i, element in enumerate(x):
    # prints the indexes and the elements of the list 
    print(i, element)

x = (4, 5, 6)

for i, element in enumerate(x):
    # prints the indexes and the elements of the list 
    print(i, element)