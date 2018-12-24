# Declare a variable and initialize it
f = 0
print (f)

# re-declaring the variable works
f = "abc"
print (f)

# ERROR: variables of different types cannot be combined
#print ("string type " + 123)
print ("string type " + str(123))

# Global vs. local variables in functions
def someFunction():
  #global f   # DO NOT USE GLOBAL FOR MODIFICATION OF DATA, BAD PRACTICE
  f = "def"
  print (f)

someFunction()
print (f) 

del f
print (f)  # Gives error as f is deleted in the preious statement
