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
      
# find() allows you to search for characters/substrings within a string
# it returns the lowest index for the characters in the string 
# and if the characters are not found it returns -1
hello = 'hello'
# prints 3
print(hello.find('ll')

# you can use find to return whether or not the characters/substrings were found with if statements
if (hello.find('ll') =! -1):
      print('Characters were found!')
else:
      print('Characters were not found :(')

# find() has second and third arguments which allow you to choose starting points
# and ending points respectively to search through

# replace() method can be used to remove/replace a character from a string
# replace function can also be used to replace multiple characters 
# and newlines or spaces
# returns string without character that was removed, or with the new characters
hello = 'hello' 
# prints heyo
print(hello.replace('ll', 'y'))

# replace() function can also have a third argument for the number of times 
# the replacement should occur (from left to right)
hello = 'helllo'
# prints heyylo
print(hello.replace('l', 'y', 2)
      
# you can also use translate() to remove/replace characters in strings
hello = 'hellao'
# prints 'hello'
print(hello.translate({ord('a'): None})
      
# to remove multiple characters, you can use translate() function and an iterator
# Note: ord() is meant to change a string or character into its respective Unicode 
# character and chr() does the opposite
# uses 'translation table' which I can only assume is a built-in dictionary that you can access
# and change the values of for your specific practice
hello = 'hellabco'
# prints 'hello'
print(hello.translate({ord(i): None for i in 'abc'})

# places the len() method onto the string
# isn't only a string method but can be used for them also SEE LISTS AND TUPLES
# argument is the object you wish to check the length of
hello = 'hello'
# prints 5 because there are 5 letters in the string
print(len(hello))

# you can also check if a string contains alphabet characters, numeric characters or both
hello = 'Hello 1'

# prints true for all
print(hello.isalpha())

print(hello.isnumeric())

print(hello.isalnum())
