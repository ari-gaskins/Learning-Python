# while loops
# while loops iterate 'while' a condition is true

x = [3, 4, 42, 3, 2, 4]
i = 0

# syntax is while condition:
# this loop will print 'run' 10 times
while i < 10:
    print('run')
    i += 1

# can also be written like this 
while True:
    print('run')
    i += 1
    if i == 10:
        break;