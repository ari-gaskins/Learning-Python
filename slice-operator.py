# Slice Operator
# slice operator allows you to take a 'slice' of a collection and manipulate it
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = 'hello'

# slice operator is written as a sequence of numbers and colons within square brackets
# the sequence is written based on start: stop: step similar to range() function SEE FOR LOOPS
sliced =  x[0:4:2]

# prints [0, 2]
print(sliced)

# slice operator can also be written with just one colon and one stop value
# also like the range() function, the stop number always returns one less than what is written
# whenever there is a blank on the left of the colon, it means start at the beginning
# whenever there is a blank on the right of the colon, it means start at the end
# whenever there are two numbers and the furthermost right of the colon is empty, 
# that means step by 1 (but you don't need to include two colons really)
sliced = x[:4]

# prints [0, 1, 2, 3]
print(sliced)

sliced = x[2:]

# prints [2, 3, 4, 5, 6, 7, 8]
print(sliced)

sliced = x[2:4]

# prints [2, 3]
print(sliced)

# like the range function you can also slice by negative steps
sliced = x[4:2:-1]

# prints [4, 3]
print(sliced)

# to easily reverse a list you can slice  like this 
sliced = x[::-1]

# prints [8, 7, 6, 5, 4, 3, 2, 1, 0]
print(sliced)

# all of these slice operations also work on strings
sliced = s[::-1]

#prints 'olleh'
print(sliced)

# slice operations work on tuples as well
sliced = (1, 2, 3, 4, 4, 2, 2, 1) [::2]

# prints steped by two so (1, 3, 4, 2)
print(sliced)