# Chained Conditional Operators
x = 7
y = 8 
z = 0

# NOTE: all conditional operators have lower precedence than arithmetic operators
# NOTE: conditional precedence is not, and, or 
result1 = x == y
result2 = y > x
result3 = z < x + 2

# or operator checks whether one side is true and returns true
# if both are false, returned boolean is false
result4 = result1 or result2 
# prints true because result2 is true
print(result4)

# and operator checks whether both sides of the conditional are true and returns true
# if one or both sides are false, returned boolean is false
result5 = result1 and result2
# prints false because result1 is false
print(result5)

# not operator turns every boolean value on the right side 
# of it to the opposite of what it originally was
# prints false
print(not True)
# prints true
print(not False)
# prints false because statement would be true
print(not (False or True))
# prints true because the statement would be false
print(not (False and True))
# prints false because statement would be true
print(not (False and True or True))

