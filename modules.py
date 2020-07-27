#module: Consider a module to be the same as a code library.
#A file containing a set of functions you want to include in your application.

"""import mymodule as mx

#You can rename modules

mymodule.greeting(" Jonathan")


a = mx.person1["age"]
print(a)
"""
#Built in functions
"""import platform

x = platform.system()
print(x)
"""

"""
import platform
#shows all the function names in the module: dir()
x = dir(platform)
print(x)
"""
"""# Can import specific dictionaries from modules
from mymodule import person1

print (person1["age"])
"""

#import date and time

import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))



#date as a object
x = datetime.datetime(2020, 5, 17)

print(x)
