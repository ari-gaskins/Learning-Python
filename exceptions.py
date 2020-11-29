# Exceptions
# this is how you raise exceptions (learn more about those later)
raise Exception('Bad')

# handling exceptions 
# use this to catch exceptions accordingly, 
# the 'Exception as e' isn't exactly required but can be used if you have specific errors
# allows you to let the code run despite errors
try: 
    x = 7 / 0
except Exception as e:
    print(e)
# you can also use a finally to close the file with some clean up code
finally:
    print('finally')