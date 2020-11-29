# Unpack Operator and *args and **kwargs

def func(*args, **kwargs):
    pass

x = [1, 23, 236363, 2727]

# the unpack operator is used to remove collections from their states and format them normally
# the unpack operator also passes them through as arguments to a function 
print(*x)

# an example of the passing through functions
def func(x, y):
    print(x, y)

# if you have a list of tuples you'd like to pass through the above function
pairs = [(1, 2), (3, 4)]

# you can pass them separately through the function by doing this 
# prints 1 2 3 4
for pair in pairs:
    func(*pair)

# you would use a double asterisk when passing a dictionary
# you don't need to name them in the correct order, so long as you name the keys the parameters
# prints 2 5
func(**{'y': 5, 'x': 2})

# *args (arguments) and **kwargs (keyword arguments) are essentially used 
# if you don't know how many arguments positional or keywords you want to accept
# they allow you to pass an unllimited amount of regular arguments or keyword arguments
def func(*args, **kwargs):
    print(args, kwargs)

# when you pass this through a function it returns a tuple and a dictionary
# (1, 2, 3, 4, 5) and {one: 0, two: 1}
# you can unpack it within the function as well if necessary
func(1, 2, 3, 4, 5, one=0, two=1)