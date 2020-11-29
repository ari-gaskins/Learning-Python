# Functions
# def keyword means define and is used to define functions
def func():
    print('run')
    # you can define functions inside functions
    def func():
        print('hi')
    func()

func()

# you can of course add parameters
def next_func(x, y):
    print('run', x, y)
    # returning more than one value will return a tuple
    return x * y, x / y

# for a cleaner look you can separate the two returned operations into two variables
r1, r2 = next_func(5, 6)

# prints 30 0.833333334
print(r1, r2)

# you can also set optional parameters that can be set to None 
# but have that overridden when necessary
def new_func(x, y, z=None):
    print(x, y, z)

# prints None for z value
new_func(1, 4)

# overrides the z value
new_func(4, 5, 2)

# its valid in python to create a function within another function
def func(x):
    def func2():
        print(x)
    return func2

# if you create a function within a function, you can call it
# by putting an extra set of parenttheses to represent the interior function
func(3)()

# you can also call func two by making a variable equal a function 
x = func(3)

# and thusly using another set of parentheses
x()