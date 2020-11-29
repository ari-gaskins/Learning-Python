# Conditional Operators
# conditions evaluates or compares two variables or data types and returns boolean value
x = 2
y = 4
# z = false, equal to operator
z = x == y
print(z)
# z = true, not equal to operator
z = x != y
print(z)
# z = true, less than or equal to operator
z = x <= y
print(z)
# z = false, greater than or equal to operator
z = x >= y
print(z)
# z = true, less than operator
z = x < y
print(z)
# z = false, greater than operator
z = x > y
print(z)

# works with strings as well 
x = 'hello'
y = 'hello'
# prints true
print(x == y)
# prints false
print(x != y)

x = 'hello'
y = 'helLo'
# prints false
print(x == y)
# prints true
print(x != y)

# can compare ordinal values (provided through ASCII)
x = 'a'
y = 'Z'
# prints true
print(x > y)
# because the ordinal value of 'a' is 97 and the ordinal value of 'Z' is 90 
# ordinal value can be checked using ord() function
print(ord(x))
print(ord(y))
