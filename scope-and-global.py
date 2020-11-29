# Scope and Global
# this variable is global and cannot be changed within a function
x = 'ari'

def func(name):
    # this variable is local and does not directly change anything outside the function
    x = name

# will print 'ari'
print(x)
func('changed')
# will still print 'ari'
print(x)

# you can change all of this using the global keyword
x = 'ari'

def func(name):
    # NOTE: not recommended to use this keyword
    global x
    x = name

# will print 'ari'
print(x)
func('changed')
# will print 'changed'
print(x)
