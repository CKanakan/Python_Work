# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.

"""
try:
    print(x)
except:
    print("An exception occurred")
"""

# In this example, the try block does not generate any error:
"""
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
"""


#Print one message if the try block raises a NameError and another for other errors:
"""
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
 """
