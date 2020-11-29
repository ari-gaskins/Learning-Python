# lambda
# a lambda is a one-line, anonymous function
# basics as shown
# NOTE: these basic examples are not the recommended way to use lambdas
x = lambda x: x + 5

# prints 7
print(x(2))

x = lambda x, y: x + y

# prints 34
print(x(2, 32))