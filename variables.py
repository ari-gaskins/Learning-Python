# Variables
hello = 'hello'

world = 'world'
# this value would be the string 'hello' when printed
world = hello

# this value would be the string 'no' when printed
hello = 'no'

# prints value of last initializations
# should print 'no hello'
print(hello, world)

# use snakecase instead of camelcase, meaning use underscores to separate words in variable names
hello_world = 'Hello world!'
# cannot start variable names with numbers or special characters