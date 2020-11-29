# if, else, and elif
x = input('Name: ')

# syntax is if condition: then enter and indent
# if condition is true, indented block is performed
if x.capitalize() == 'Ari':
    print('You are great!')
# elif is shortened 'else if' and must be after if and before else
# allows for another condition to be checked for true
# you can have as many elifs as you want, but only one if and one else
elif x.capitalize() == 'Joe':
    print('Bye Joe')
elif x.capitalize() == 'Sarah':
    print('Hello Sarah ;)')
# if all conditions are false, the indented block after else is performed
else:
    print('No')

print('Always do this')