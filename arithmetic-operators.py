# arithmetic operators
# can only perform arithmetic with the same data types or as long as they are both numbers
x = 9
y = 3
# add
result = x + y
# multiply
result = x * y 
# whenever you divide, the compiler returns a float
# divide
result = x / y
# if you don't want to have a float you can convert to an integer like this
# divide and return an integer
result = int(x / y)
# subtract
result = x - y
# create exponent raises x to the power y (x^y)
result = x ** y
# this will give the integer result of whatever the division is
# removing all decimal points i.e. remainder
# floor division
result = x // y
# returns the remainder after division
# modulo
result = x % y
# you can use parentheses to utilize order of operations
result = (x + y) * 2

print(result)

num = input('Number: ') 
# if receiving user input, must use int() or float() function to convert from string
print(int(num) - 5)

# if there is one float as an operand in arithmetic, float will always be returned

# String multiplication and addition
# you can multiply a string by an integer
x = 'NIGHTMARE'
y = 3
# prints 'NIGHTMARE', 3 times
# NOTE: string must be left hand side, cannot put 3 * 'NIGHTMARE'
print(x * y)

# addition with strings is concatenation
x = 'hello'
y = 'world'
# prints 'helloworld' 
print(x + y)