# String Methods
hello = 'hello'
# prints the data type of the object using the type() function
print(type(hello))

# places the upper() string method onto the string
# returns the string as all uppercase
hello = 'hello'.upper()
# prints 'HELLO'
print(hello)
# OR
hello = 'hello'
# prints 'HELLO' also
print(hello.upper())

# places the lower() string method onto the string
# returns the string as all lowercase
hello = 'HELLO'.lower()
# prints 'hello'
print(hello)
# OR
hello = 'HELLO'
# prints 'hello' also
print(hello.lower())
# upper() and lower() are useful when receiving user input and seeking certain validations

# places the capitalize() string method onto the string 
# returns the string with a capitalized first letter AND removes caps from elsewhere
hello = 'hello'.capitalize()
# prints 'Hello'
print(hello)
# OR 
hello = 'hello'
# prints 'Hello' also
print(hello.capitalize())

# places the count() string method onto the string
# returns how many instances of a certain character or characters are in a given string
# argument is the phrase you wish to search for
# NOTE: formatting is important, upper and lowercase is accounted for
hello = 'hello'.count('ll')
# prints 1
print(hello)
# OR 
hello = 'hello'
# prints 1 also
print(hello.count('ll'))

# you can also double up on string methods
hello = 'heLLo'
# prints 1 (changes to lowercase first to allow proper count)
print(hello.lower().count('ll'))

# places the len() method onto the string
# isn't only a string method but can be used for them also SEE LISTS AND TUPLES
# argument is the object you wish to check the length of
hello = 'hello'
# prints 5 because there are 5 letters in the string
print(len(hello))