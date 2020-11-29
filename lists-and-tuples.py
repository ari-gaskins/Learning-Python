# Lists and Tuples
# LISTS

# a list is denoted by square brackets
# inside a list there are a series of elements which are some data types 
# NOTE: elements do not have to be the same data type
# list is an ordered collection, meaning order is stored and maintained, kind of like arrays
# list is defined like this, but can also be defined as empty which is just empty brackets
x = [4, True, 'hi']
# prints the length of the list using len() function, therefore prints 3
print(len(x))
# length function len() can also be used for strings SEE STRING METHODS

# append() function adds to the end of the list 
# argument is the object you wish to add to the end of the list
hello = 'hello'
x.append(hello)
# prints full list in square brackets, with string 'hello' added to the end
print(x)

# extend() function adds another list to the end of the current list
# argument is another list that you would to append your list with
y = ['right', 'left', 5, 6.7]
x.extend(y)
# prints x list + y list
print(x) 

# pop() function removes last item from the list and returns it 
# prints 6.7
print(x.pop())
# NOTE: 6.7 is now removed from the list

# if there is an argument, it is the index of the object you wish to remove
# NOTE: list indexes are counted the same way as arrays, starting with 0 (zero)
# prints 4, because it is the first element in the list and it's index is 0
print(x.pop(0))
# NOTE: 4 is now removed from the list and the index of each element has changed

# if you want to access an element in a list use square brackets 
# with an argument of the index of the element you wish to access
# prints string 'hi'
print(x[1])

# you can also change the value of an element in the list by using # the same square brackets and index
x[4] = 11
# prints new list with last element as 11
print(x)

# NOTE: variables assigned to lists do not store a copy of the list they serve as a reference to the list
# this is why they are considered 'mutable' or editable, essentially
# the items of the list are stored on the heap
new_list = ['left', 'middle', 'right']
list_now = new_list
new_list[1] = 'center'
# prints the same list because the variable is a reference, not a copy
print(new_list, list_now)

# to copy a list 
new_list = ['left', 'middle', 'right']
# we use square brackets with argument : (colon)
list_now = new_list[:]
new_list[1] = 'center'
# prints different lists because the list_now copied the original
print(new_list, list_now)

# you can also have tuples and lists inside of lists and more lists and tuples inside of those lists
x = [[3, 'nine', 1000], ('z', 'f', 'h'), ['best', 'worst', 15]]
# prints all elements
print(x)

# TUPLES

# tuples are similar to lists, except they are immutable, as in elements cannot be changed
# tuples use round brackets
x = (0, 0, 2, 2)
# prints full tuple
print(x)

# can access elements the same as lists CANNOT CHANGE THEM MUST REDEFINE TO CHANGE
# prints first element of tuple
print(x[0])

# cannot use append() or extend() functions with tuples


